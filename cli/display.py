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
    penalty_messages = result.get("penalty_messages", [])

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

    if penalty_messages:
        print("\n⚠️ RESOURCE PENALTIES")
        print("--------------------------------------------------")
        for message in penalty_messages:
            print(f"- {message}")

    print("==================================================")

    input("\nPress Enter to continue...")




def display_action_selected_message(action: str):
    messages = {
        "rest": "🛌 You chose to rest. Your team takes a moment to recover.",
        "work_on_product": "💻 You chose to work on the product. Time to build, fix, and improve.",
        "marketing_push": "📢 You launch a marketing push to build excitement around your startup.",
        "travel": "🚗 You chose to travel. Every mile brings you closer to San Francisco.",
        "buy_coffee": "☕ You bought coffee. The team is ready to keep going.",
        "save": "💾 Progress saved. Your journey can continue later.",
        "abandon": "❌ This run comes to an end.",
    }

    message = messages.get(action)

    if message:
        print(f"\n{message}")
       
def display_game_over(game: dict):
    print("\n==================================================")
    print("                 💔 GAME OVER 💔")
    print("==================================================\n")

    print("Your startup could not survive the journey.\n")

    print("Final status:")
    print("--------------------------------------------------")
    print(f"📍 Location: {game.get('current_location')}")
    print(f"🛣️  Progress: {game.get('travel_progress')}%")
    print(f"💰 Cash: {game.get('cash')}")
    print(f"⚡ Team Energy: {game.get('team_energy')}")
    print(f"☕ Caffeine: {game.get('caffeine')}")
    print(f"📈 Market Traction: {game.get('market_traction')}")
    print(f"🐛 Bug Count: {game.get('bug_count')}")
    print("--------------------------------------------------\n")

    if game.get("team_energy", 0) <= 0:
        print("Reason: Your team ran out of energy.")
    elif game.get("cash", 0) <= 0:
        print("Reason: Your startup ran out of cash.")
    else:
        print("Reason: Your startup was unable to continue.")

    print("\nBetter luck on the next run, founder.")
    print("==================================================\n")

    input("Press Enter to return to the main menu...")



def display_victory(game: dict):
    print("\n==================================================")
    print("         🎉 YOU MADE IT TO SAN FRANCISCO! 🎉")
    print("==================================================\n")

    print("Your startup reached San Francisco and made it")
    print("to the big pitch. Congratulations, founder!\n")

    print("Final status:")
    print("--------------------------------------------------")
    print(f"📍 Final Location: {game.get('current_location')}")
    print(f"🛣️ Progress: {game.get('travel_progress')}%")
    print(f"💰 Cash: {game.get('cash')}")
    print(f"⚡ Team Energy: {game.get('team_energy')}")
    print(f"☕ Caffeine: {game.get('caffeine')}")
    print(f"📈 Market Traction: {game.get('market_traction')}")
    print(f"🐛 Bug Count: {game.get('bug_count')}")
    print("--------------------------------------------------\n")

    print("You survived the journey and kept your startup alive.")
    print("That pitch could change everything.")
    print("==================================================\n")

    input("Press Enter to return to the main menu...")




def display_rules():
    print("\n==================================================")
    print("📜 GAME RULES")
    print("==================================================\n")

    print("🎯 Objective:")
    print("Travel from San Jose to San Francisco and reach your final pitch.\n")

    print("⚙️ Resources:")
    print(" ✔︎ Cash              - Needed to survive and perform actions")
    print(" ✔︎ Team Energy       - If it reaches 0, you lose")
    print(" ✔︎ Caffeine          - Helps sustain your team")
    print(" ✔︎ Market Traction   - Represents your startup’s momentum")
    print(" ✔︎ Bug Count         - Too many bugs can hurt progress")
    print(" ✔︎ Travel Progress   - Reach 100% to win\n")

    print("🎮 Actions:")
    print(" ✔︎ Rest              - Recover energy (uses caffeine)")
    print(" ✔︎ Work on Product   - Reduce bugs, but costs energy")
    print(" ✔︎ Marketing Push    - Increase traction, but costs cash")
    print(" ✔︎ Travel            - Move forward (affected by weather & traffic)")
    print(" ✔︎ Buy Coffee        - Restore caffeine (costs cash)\n")

    print("⚠️ Game Over Conditions:")
    print(" ✔︎ Team Energy reaches 0")
    print(" ✔︎ Cash reaches 0\n")

    print("🏆 Victory Condition:")
    print(" ✔︎ Reach 100% travel progress (arrive in San Francisco)\n")

    print("🎲 Events:")
    print("Random events may occur during your journey and require decisions.\n")

    print("==================================================\n")

    input("Press Enter to return to the menu...")