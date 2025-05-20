
import flax.linen as nn
import jax
import jax.numpy as jnp
from einops import rearrange, reduce, repeat
from jax.random import split


class NCANetwork(nn.Module):
    d_state: int = 16
    @nn.compact
    def __call__(self, x):
        x = jnp.pad(x, pad_width=1, mode='wrap')
        x = nn.Conv(features=4, kernel_size=(3, 3), padding="VALID")(x)
        x = nn.Conv(features=16, kernel_size=(1, 1))(x)
        x = nn.relu(x)
        x = nn.Conv(features=self.d_state, kernel_size=(1, 1))(x)
        return x


class NCA():
    def __init__(self, grid_size=64, d_state=16, p_drop=0.0, dt=0.01):
        self.grid_size = grid_size
        self.d_state = d_state
        self.nca = NCANetwork(d_state=d_state)
        self.p_drop = p_drop
        self.dt = 0.01

    def default_params(self, rng):
        # rng, _rng = split(rng)
        # color_map = jax.random.normal(_rng, (self.n_groups, self.d_state, 3)) # unconstrainted
        rng, _rng = split(rng)
        net_params = self.nca.init(_rng, jnp.zeros((self.grid_size, self.grid_size, self.d_state))) # unconstrainted
        return dict(net_params=net_params)
    
    def init_state(self, rng, params):
        state = jax.random.uniform(rng, (self.grid_size, self.grid_size, self.d_state), minval=0, maxval=1)
        return state
    
    def step_state(self, rng, state, params):
        dstate = self.nca.apply(params['net_params'], state)

        mask = 1. - jnp.floor(jax.random.uniform(rng, state.shape[:2], minval=0, maxval=1) + self.p_drop)
        dstate = dstate * mask[..., None]

        state = state + dstate * self.dt
        state = jnp.clip(state, 0, 1)
        return state
    
    def render_state(self, state, params, img_size=None):
        assert self.d_state == 1 or self.d_state == 3
        if self.d_state == 1:
            zeros = jnp.zeros_like(state)
            img = jnp.concatenate([state, zeros, zeros], axis=-1)
        else:
            img = state
        if img_size is not None:
            img = jax.image.resize(img, (img_size, img_size, 3), method='nearest')
        return img

