import httpx

CNB_URL ="https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

def get_exchange_rate():
    try:
        response = httpx.get(CNB_URL)
        response.raise_for_status()
        lines = response.text.split("\n")
        for line in lines:
            if "EUR" in line:
                return float(line.split("|")[-1].replace(",", "."))
    except httpx.HTTPError as e:
        print(f"Chyba při stahování kurzu: {e}")
    return None

def convert_currency(amount, rate, direction):
    if direction == "EUR->CZK":
        return amount * rate
    elif direction == "CZK->EUR":
        return amount / rate

def main():
    rate = get_exchange_rate()
    if rate is None:
        print("Nepodařilo se získat kurzovní lístek. Zkuste to později.")
        return
    
    print(f"Aktuální kurz EUR/CZK: {rate:.2f}")

    while True:
        direction = input("Zvolte směr převodu (EUR->CZK nebo CZK->EUR, pro ukončení napište 'exit'): ").strip()
        if direction.lower() == "exit":
            print("Děkujeme za použití směnárny.")
            break
        elif direction not in ("EUR->CZK", "CZK->EUR"):
            print("Neplatná volba. Zkuste to znovu.")
            continue

        try:
            amount = float(input("Zadejte částku k převodu: ").strip())
            if amount < 0:
                print("Částka musí být kladné číslo.")
                continue
        except ValueError:
            print("Neplatný vstup. Zadejte prosím číslo.")
            continue

        result = convert_currency(amount, rate, direction)
        print(f"Výsledek převodu: {result:.2f} {'CZK' if direction == 'EUR->CZK' else 'EUR'}\n")

if __name__ == "__main__":
    main()
