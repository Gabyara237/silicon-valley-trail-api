def display_option_title(option: str):
    print("\n====================================")
    print(f"             {option}               ")
    print("====================================\n\n")


def display_game_status(game: dict):
    print("\n==================================================")
    

    print(f"Day {game.get('current_day', 1)} | {game.get('current_location')}")
    print("Your startup's humble garage HQ")
    
    print("==================================================")
    print(
        f"💰 Cash: ${game.get('cash')} | "
        f"⚡ Energy: {game.get('team_energy')}/100 | "
        f"☕ Caffeine: {game.get('caffeine')}"
    )
    print(
        f"📈 Traction: {game.get('market_traction')}/100 | "
        f"🐛 Bugs: {game.get('bug_count')}"
    )
    print(
        f"📍 Progress: {game.get('travel_progress')}% to San Francisco"
    )

    print("==================================================\n")



def display_game_intro():
    print("\n==============================================")
    print("        🚀 The Road to San Francisco 🚀")
    print("==============================================\n")

    print("Your startup team is beginning a bold journey")
    print("from San Jose to San Francisco.")
    print("The goal: reach your final pitch and secure funding")
    print("before your resources run out.\n")

    print("To succeed, you'll need to manage your resources carefully:\n")
    print(" 💰 Cash             - Keep your startup running")
    print(" ⚡ Team Energy       - Avoid burnout")
    print(" ☕ Caffeine          - Essential fuel for the grind")
    print(" 📈 Market Traction   - Build momentum and visibility")
    print(" 🐛 Bug Count         - Keep your product stable")

    print("Every decision matters.")
    print("Make it to San Francisco… or risk losing everything.\n\n")

    display_press_enter_message()



def display_press_enter_message():
    print("==============================================\n")
    input("Press Enter to begin your journey...")