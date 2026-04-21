# 🚀 Silicon Valley Trail

![Python](https://img.shields.io/badge/python-3.12-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/framework-FastAPI-009688?logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red)
![PostgreSQL](https://img.shields.io/badge/database-PostgreSQL-336791?logo=postgresql&logoColor=white)
![CLI](https://img.shields.io/badge/interface-CLI-lightgrey)
![JWT](https://img.shields.io/badge/auth-JWT-blue)

**Silicon Valley Trail** is a strategy-based simulation game inspired by *The Oregon Trail*, where players manage a startup team traveling through Silicon Valley to reach San Francisco and secure a life-changing pitch.

The project consists of:
- A **FastAPI backend** with game logic and persistence
- A **CLI frontend** that acts as the interactive game interface

---
 
## Demo
 
> Travel action with real-time weather data (Open-Meteo), traffic simulation (Google Routes API), a random event trigger, and an AI strategy recommendation powered by Google Gemini — all in a single run.
 
https://github.com/user-attachments/assets/2c8e31ca-9b0d-46fd-830b-3072765c4171
 
---

## Description

In Silicon Valley Trail, players must carefully manage resources while making strategic decisions that affect their startup's survival. Each turn brings new challenges — unexpected events, shifting weather, and real traffic conditions that influence your journey.

The game is built as a distributed system: the backend handles all state, logic, and persistence, while the CLI client communicates with it over HTTP, acting as a true frontend consumer of the API.

---

## Project Links

- **Backend Repository:**
  [View the Silicon Valley Trail API on GitHub](https://github.com/Gabyara237/silicon-valley-trail-api)

---
 
## Screenshots
 
### Entry point
The main menu supports three player paths - login, register, or instant guest play — each routing to a different backend flow.

![Welcome screen](https://i.postimg.cc/7hqMJR0G/welcome.png)


### Guest game menu  
Guest users see a simplified version of the menu, with core gameplay actions only. Features like save/resume, AI strategy advice, and traffic-aware travel are available only to authenticated users.

![Guest game menu](https://i.postimg.cc/XqncBPdy/game-menu-guest.png)

### Authenticated game menu
Logged-in users get the full feature set: save/resume sessions, AI strategy advice, and traffic-aware travel. 
 
![Authenticated game menu](https://i.postimg.cc/yx7X3Gc0/game-menu-auth.png)
 
### Save & resume flow
Game state is fully persisted in PostgreSQL. Players can save mid-run and resume exactly where they left off across sessions.
 
![Saving a game](https://i.postimg.cc/WtLV7Mpt/save-game.png)
 
![Resuming a saved game](https://i.postimg.cc/qgVrG8Bz/resume-game.png)
 
### AI Strategy Advisor
The AI advisor analyzes the current game state and recommends the best next action with a brief explanation. Available to authenticated users only.
 
![AI Strategy Advice response](https://i.postimg.cc/3W5hZgrR/ai-advice.png)
 
### Real-time travel updates
The Travel action pulls live data from Open-Meteo (weather) and Google Routes API (traffic). Both modifiers are applied to resource changes and displayed to the player before the next turn.
 
![Weather and traffic updates during travel](https://i.postimg.cc/MHzbfLVV/travel-updates.png)
 
### Random event system
Events are triggered after travel actions. Each event presents a contextual scenario with 2–3 choices, and the player's decision directly affects their resource state.
 
![Random event: Coffee Shortage](https://i.postimg.cc/ZnJFvQpd/random-event.png)
 
### Win & loss screens
The game tracks all six resources continuously. Reaching 100% travel progress triggers the victory screen; energy or cash hitting zero ends the run.
 
![Victory — startup reaches San Francisco](https://i.postimg.cc/4xHtyGq1/victory.png)
 
![Game over — team runs out of energy](https://i.postimg.cc/BbJcPzHP/game-over.png)
 
---

## Core Features

- Turn-based decision system with resource management
- JWT-based authentication with guest mode support
- Random event system with player choices that affect game state
- Optional AI strategy advisor powered by **Google Gemini**
- External API integrations:
  - **Open-Meteo API** – real weather data influencing gameplay
  - **Google Routes API** – traffic simulation with fallback system
  - **Google Gemini API** – AI-generated strategy recommendations
- Game state persistence with save, resume, and abandon support
- Async backend with full PostgreSQL persistence via SQLAlchemy


## Resources & Game States

Players manage six core resources throughout the journey:

| Resource |  Role |
|---|---|
| Cash |  Primary currency for actions and supplies |
| Team Energy |  Depleted by work; game over if it hits 0 |
| Caffeine |  Consumed by rest and work actions |
| Market Traction |  Increases through marketing pushes |
| Bug Count |  Reduced by working on the product |
| Travel Progress |  Reaches 100% to win the game |

**Game states:** `in_progress` · `saved` · `won` · `lost` · `abandoned`


## Win & Loss Conditions

**Victory:** Reach **100% travel progress** and arrive in San Francisco.

**Game Over:**
- Team Energy reaches **0**
- Cash reaches **0**


## Available Actions

| Action | Effect |
|---|---|
| Rest | Recover energy (consumes caffeine) |
| Work on Product | Reduce bugs (costs energy & caffeine) |
| Marketing Push | Increase traction (costs cash) |
| Travel | Progress forward (affected by weather & traffic) |
| Buy Coffee | Restore caffeine (costs cash) |
| Save Game | Persist current game state |
| Abandon Game | End the current run |


## Guest Mode vs Authenticated Users

The game supports two types of players, each with a different feature set:

| Feature | Guest | Authenticated |
|---|---|---|
| Instant play (no signup) | ✔︎ | ✔︎ |
| Save & resume sessions | ✖︎ | ✔︎ |
| AI strategy advisor | ✖︎ | ✔︎ |
| Traffic simulation | ✖︎ | ✔︎ |
| Full event system | ✔︎ | ✔︎ |

Guest mode is stateless by design, game state is passed directly in the request body with no persistence. This allows players to try the game immediately while keeping the authenticated experience as the full feature set.


## API Routes Overview

### Authentication
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| `POST` | `/auth/sign-up` | Register a new user | Public |
| `POST` | `/auth/sign-in` | Login and receive JWT token | Public |
| `GET` | `/auth/me` | Get current authenticated user | Required |

### Games (Authenticated)
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| `POST` | `/games/new` | Create a new game session | Required |
| `GET` | `/games/active` | Get the user's current active game | Required |
| `POST` | `/games/{game_id}/actions` | Submit a player action | Required |
| `POST` | `/games/{game_id}/events` | Submit a player event choice | Required |
| `POST` | `/games/{game_id}/save` | Save the current game | Required |
| `POST` | `/games/{game_id}/resume` | Resume a saved game | Required |
| `POST` | `/games/{game_id}/abandon` | Abandon the current game | Required |
| `POST` | `/games/{game_id}/ai-advice` | Get AI-generated strategy recommendation | Required |

### Games (Guest Mode)
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| `POST` | `/games/guest` | Create a stateless guest game session | Public |
| `POST` | `/games/guest/actions` | Submit an action to a guest game | Public |
| `POST` | `/games/guest/events` | Submit an event choice to a guest game | Public |

> Protected routes require a valid JWT token in the `Authorization: Bearer <token>` header.
> Guest mode is stateless, game state is passed directly in the request body with no persistence.


## Entity Relationship Diagram (ERD)

![Silicon Valley Trail ERD](https://i.postimg.cc/jqQ6b8KT/ERD.png)

The database consists of three tables with the following relationships:
- A `users` record can have many `games` (one-to-many)
- A `games` record can have many `game_events` (one-to-many)


### Schema Enforcement

The database enforces:
- Foreign key relationships with `ON DELETE CASCADE`
- `NOT NULL` constraints on all gameplay resources
- `UNIQUE` constraints on `username` and `email`
- Enum-typed columns for `status`, `current_location`, `event_type`, and `player_choice`
- Automatic timestamping on all tables

### Enum Definitions

**`GameStatus`** — game lifecycle states
```
in_progress | won | lost | abandoned | saved
```

**`Location`** — travel checkpoints from start to finish
```
San Jose → Santa Clara → Sunnyvale → Mountain View → Palo Alto
→ Menlo Park → Redwood City → San Mateo → Burlingame → San Francisco
```

**`EventType`** — categories of random events
```
hackathon | bugs | networking | feature_request | coffee_shortage
```

**`EventChoice`** — player response options per event
```
accept | reject | attend | ignore | build | buy | skip
```

---

## AI Strategy Advisor

Silicon Valley Trail includes an optional AI-powered strategy advisor built with **Google Gemini**. Players can request real-time recommendations based on their current game state.

The advisor analyzes:
- Cash, Team Energy, and Caffeine levels
- Market Traction and Bug Count
- Travel Progress

It suggests the best next action from the available options and briefly explains the reasoning behind the recommendation.

### Implementation Details

- Integrated through a dedicated AI service layer, isolated from core game logic
- Includes retry logic for transient failures (e.g., 503 errors)
- Falls back to predefined advice if the AI service is unavailable
- The feature is entirely optional — the game remains fully functional without it

### Design Philosophy

The AI layer is intentionally non-critical. Core gameplay is deterministic and self-contained; Gemini is used purely as an advisory enhancement. This separation ensures reliability while still offering a richer experience for authenticated users.



## Technologies Used

### Backend
- **Python 3.12**
- **FastAPI** – async web framework
- **SQLAlchemy (async)** – ORM and database management
- **PostgreSQL** – relational database
- **JWT Authentication** – secure user sessions

### CLI
- **Python** – modular CLI interface
- **httpx** – async HTTP client for API communication

### External APIs
- **Open-Meteo API** – real-time weather data
- **Google Routes API** – traffic simulation with fallback
- **Google Gemini API** – AI-generated strategy advice


## Testing

Unit tests implemented with **pytest** covering:

- Win and loss conditions
- Resource-based state transitions
- Coordinate mapping between locations
- Action effects (e.g., Buy Coffee resource update)

Run tests with:

```bash
pytest
```


## Project Structure

```
silicon-valley-trail-api/
├── app/
│ ├── core/ # Game logic and rules engine
│ ├── database/ # Database configuration and session management
│ ├── integrations/ # Weather, traffic & AI API clients
│ ├── models/ # SQLAlchemy models
│ ├── routes/ # FastAPI route definitions
│ ├── schemas/ # Pydantic schemas
│ ├── services/ # Business logic layer
│ ├── config.py # App configuration (env variables)
│ ├── dependencies.py # Dependency injection
│ └── main.py # FastAPI entry point
│
├── cli/
│ ├── main.py # CLI entry point
│ ├── api_client.py # HTTP client to communicate with backend
│ ├── display.py # CLI output formatting
│ ├── handlers.py # High-level flow coordination
│ ├── game_loop.py # Core game loop
│ ├── game_handlers.py # Game actions and event handlers
│ ├── menus.py # CLI menus
│ ├── prompts.py # User input handling
│ └── utils.py # Helper functions
│
├── tests/ # Unit tests
│ └── test_game_logic.py
│
├── .env.example # Example environment configuration
├── requirements.txt # Project dependencies
├── pytest.ini # Pytest configuration
└── README.md
```


## Getting Started
 
### Prerequisites
 
- Python 3.11+
- PostgreSQL

### 1. Clone the repository
 
```bash
git clone https://github.com/Gabyara237/silicon-valley-trail-api
cd silicon-valley-trail-api
```
 
### 2. Create virtual environment
 
```bash
python -m venv venv
source venv/bin/activate
```
 
### 3. Install dependencies
 
```bash
pip install -r requirements.txt
```
 
### 4. Configure environment variables
 
Create a `.env` file in the root directory:
 
```bash
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=silicon_valley_trail
 
JWT_SECRET=your_secret_key
JWT_ALGORITHM=HS256
 
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
GEMINI_API_KEY=your_gemini_api_key
```
 
### 5. Run the backend
 
```bash
fastapi dev
```
 
The API will be available at `http://localhost:8000`
 
Interactive API docs: `http://localhost:8000/docs`
 
### 6. Run the CLI
 
```bash
python -m cli.main
```
 
## Game Flow

1. User registers or plays as guest
2. Game session is created or resumed
3. Player selects actions in the CLI
4. Backend processes the action:
   - Applies resource effects
   - Checks win/loss conditions
   - Triggers random events
   - Applies weather and traffic modifiers
5. CLI displays the updated game state
6. Player continues, saves, or exits


## Current Implementation Notes

- **Authentication** uses JWT tokens with optional guest mode for sessionless play
- **Game state** is fully persisted in PostgreSQL, supporting save/resume across sessions
- **Event system** generates contextual random events with branching player choices
- **Traffic simulation** uses Google Routes API with a built-in fallback for offline/dev environments
- **Weather integration** pulls real-time data from Open-Meteo and applies travel modifiers
- **AI advisor** is implemented as an isolated service layer with retry logic and graceful fallback, core gameplay is never blocked by AI availability


## Future Improvements

- Build a React web frontend for a more interactive and user-friendly experience
- Add difficulty levels to make the game more dynamic and replayable
- Allow logged-in users to view all of their previous game sessions
- Create a personal statistics dashboard showing wins, losses, abandoned games, and saved games
- Implement a Top 3 players leaderboard based on performance
