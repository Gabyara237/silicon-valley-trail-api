def display_option_title(option: str):
    print("\n====================================")
    print(f"             {option}               ")
    print("====================================\n\n")


def display_game_status(game: dict):
    print("\n==================================================")
    

    print(f"Day {game.get('current_day', 1)} | {game.get('current_location')}")
    
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
    print(" 🐛 Bug Count         - Keep your product stable\n")

    print("Every decision matters.")
    print("Make it to San Francisco… or risk losing everything.\n\n")

    display_press_enter_message()



def display_press_enter_message():
    print("==============================================\n")
    input("Press Enter to begin your journey...")


def display_action_feedback(result: dict):
    weather_description = result.get("weather_description")
    traffic_description = result.get("traffic_description")

    if not (weather_description or traffic_description):
        return

    print("\n==================================================")

    if weather_description:
        print("\n🌤️  WEATHER UPDATE")
        print("--------------------------------------------------")
        print(f"  {weather_description}\n")

    if traffic_description:
        print("\n🚦 TRAFFIC UPDATE")
        print("--------------------------------------------------")
        print(f"  {traffic_description}\n")

    print("==================================================")

    input("\nPress Enter to continue...")




def display_action_selected_message(action: str):
    messages = {
        "rest": "🛌 You chose to rest. Your team takes a moment to recover.",
        "work_on_product": "💻 You chose to work on the product. Time to build, fix, and improve.",
        "marketing_push": "📢 You launch a marketing push to build excitement around your startup.",
        "travel": "🚗 You chose to travel. Every mile brings you closer to San Francisco.",
        "save": "💾 Progress saved. Your journey can continue later.",
        "abandon": "❌ This run comes to an end.",
    }

    message = messages.get(action)

    if message:
        print(f"\n{message}")
       