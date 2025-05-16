import hashpumpy
import sys

def perform_attack():
    # Intercepted message and MAC from server.py
    intercepted_message = b"amount=100&to=alice"
    intercepted_mac = "614d28d808af46d3702fe35fae67267c"  # MAC from server.py
    data_to_append = b"&admin=true"
    key_length = 14  # Length of 'supersecretkey'

    # Print inputs for debugging
    print("Intercepted message:", intercepted_message)
    print("Intercepted MAC:", intercepted_mac)
    print("Data to append:", data_to_append)
    print("Key length:", key_length)

    try:
        # Perform length extension attack
        forged_mac, forged_message = hashpumpy.hashpump(
            intercepted_mac,      # Original MAC
            intercepted_message,  # Original message
            data_to_append,       # Data to append
            key_length            # Guessed key length
        )

        print("Forged message:", forged_message)
        print("Forged MAC:", forged_mac)

        # Save forged message and MAC for verification
        with open("forged_output.txt", "w") as f:
            f.write(f"Forged message: {forged_message}\n")
            f.write(f"Forged MAC: {forged_mac}\n")
    except Exception as e:
        print(f"Error during attack: {e}")

if __name__ == "__main__":
    perform_attack()
