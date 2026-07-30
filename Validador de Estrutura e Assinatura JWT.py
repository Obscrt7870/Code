import base64
import json 

def parse_jwt_unverified(token: str):
    try:
        parts = token.split('.')
        if len(parts) != 3:
            raise ValueError("Formato de token JWT inválido.")

        def decode_component(part):
            # Corrige o padding do Base64Url
            padded = part + '=' * (-len(part) % 4)
            data = base64.urlsafe_b64decode(padded)
            return json.loads(data)

        header = decode_component(parts[0])
        payload = decode_component(parts[1])

        print("=== HEADER ===")
        print(json.dumps(header, indent=2))
        print("\n=== PAYLOAD ===")
        print(json.dumps(payload, indent=2))

    except Exception as e:
        print(f"[-] Erro ao decodificar JWT: {e}")

if __name__ == "__main__":
    sample_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkF1ZGl0b3IiLCJhZG1pbiI6dHJ1ZSwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    parse_jwt_unverified(sample_jwt)
