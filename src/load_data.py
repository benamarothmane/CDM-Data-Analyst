<<<<<<< HEAD
import pandas as pd
from .config import RAW_DATA

def load_matches() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA / "WorldCupMatches.csv")

def load_players() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA / "WorldCupPlayers.csv")

def load_scorers() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA / "GoalScorers.csv")
=======
import pandas as pd
from .config import RAW_DATA

def load_matches() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA / "WorldCupMatches.csv")

def load_players() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA / "WorldCupPlayers.csv")

def load_scorers() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA / "GoalScorers.csv")
>>>>>>> a9be46c388157bd76f69a7d44f5ea069ebc7001d
