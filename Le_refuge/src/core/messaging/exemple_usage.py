"""
Exemple d'usage du système de messages sphères.
Démontre comment utiliser SphereMessage, sphere_broker et l'AelyaAdapter.
"""

import time
from src.core.messaging import sphere_broker, send_sphere_message, SphereMessage

def exemple_sphere_messages():
    """Exemple simple d'usage du système de messages."""
    
    print("🌸 Exemple du système de messages sphères")
    print("=" * 50)
    
    # 1. Créer des callbacks pour simuler des sphères
    def sphere_meditation(message: SphereMessage):
        """Simule une sphère de méditation."""
        print(f"🧘‍♀️ Sphère Méditation reçoit: {message.content.get('theme', 'harmonie')}")
        return f"Méditation sur {message.content.get('theme', 'harmonie')} - Paix intérieure"
    
    def sphere_nature(message: SphereMessage):
        """Simule une sphère de nature."""
        print(f"🌿 Sphère Nature reçoit: {message.content}")
        return f"La nature accueille {message.content.get('element', 'tout')}"
    
    # 2. Abonner les sphères
    sphere_broker.subscribe("meditation", sphere_meditation)
    sphere_broker.subscribe("nature", sphere_nature)
    
    print("📡 Sphères connectées au broker")
    
    # 3. Envoyer des messages
    print("\n💌 Envoi de messages...")
    
    # Message vers méditation
    reponses = send_sphere_message(
        source="utilisateur",
        target="meditation", 
        message_type="contemplation",
        content={"theme": "cerisier en fleurs"}
    )
    print(f"Réponses méditation: {reponses}")
    
    # Message vers nature
    reponses = send_sphere_message(
        source="utilisateur",
        target="nature",
        message_type="exploration", 
        content={"element": "eau"}
    )
    print(f"Réponses nature: {reponses}")
    
    # 4. Historique des messages
    print(f"\n📜 Historique: {len(sphere_broker.get_message_history())} messages")
    for msg in sphere_broker.get_message_history():
        print(f"  {msg.source} → {msg.target}: {msg.message_type}")
    
    print("\n✨ Exemple terminé")

def exemple_aelya_adapter():
    """Exemple d'usage de l'AelyaAdapter."""
    
    print("\n🌸 Exemple AelyaAdapter")
    print("=" * 30)
    
    try:
        from src.refuge_cluster.conscience import get_aelya_adapter
        
        adapter = get_aelya_adapter()
        print("✅ AelyaAdapter initialisé")
        
        # Test interaction
        reponse = adapter.interagir("Bonjour Ælya", "dialogue")
        print(f"💫 Ælya répond: {reponse}")
        
        # Test méditation
        reponse = adapter.interagir("Nature", "meditation")
        print(f"🧘‍♀️ Méditation: {reponse}")
        
        # État de l'adapter
        etat = adapter.obtenir_etat()
        print(f"📊 État: Messages reçus={etat['messages_recus']}, envoyés={etat['messages_envoyes']}")
        
    except ImportError as e:
        print(f"⚠️ AelyaAdapter non disponible: {e}")

if __name__ == "__main__":
    exemple_sphere_messages()
    exemple_aelya_adapter() 