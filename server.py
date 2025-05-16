import hashlib

SECRET_KEY = b'supersecretkey'  # Unknown to attacker
def generate_mac(message: bytes) -> str:
    return hashlib.md5(SECRET_KEY + message).hexdigest()

def verify(message: bytes, mac: str) -> bool:
    expected_mac = generate_mac(message)
    return mac == expected_mac

def main():
    # Example message
    message = b"amount=100&to=alice"
    mac = generate_mac(message)
    print("=== Server Simulation ===")
    print(f"Original message: {message.decode()}")
    print(f"MAC: {mac}")
    print("\n--- Verifying legitimate message ---")
    if verify(message, mac):
        print("MAC verified successfully. Message is authentic. \n")
    # Simulated attacker-forged message
    forged_message = b"amount=100&to=alice\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x01\x00\x00\x00\x00\x00\x00&admin=true"
    forged_mac = "97312a73075b6e1589117ce55e0a3ca6"
    print(f"Forged message (hex): {forged_message.hex()}")
    print("--- Verifying forged message ---")
    computed_mac = generate_mac(forged_message)
    print(f"Computed MAC for forged message: {computed_mac}")
    print(f"Expected forged MAC: {forged_mac}")
    if verify(forged_message, forged_mac):
        print("MAC verified successfully (unexpected).")
    else:
        print("MAC verification failed (as expected).")

if __name__ == "__main__":
    main()
