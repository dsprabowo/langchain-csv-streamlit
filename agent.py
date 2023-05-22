from dotenv import load_dotenv
from langchain import OpenAI
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd

# Setting up the api key

load_dotenv()


def generate_agent(filename: str):
    llm = OpenAI(temperature = 0)
    df = pd.read_csv(filename)
    return create_pandas_dataframe_agent(llm, df, verbose=True)


def agent_query(agent, query):
    prompt = (
        query
    )

    # Run the prompt through the agent.
    response = agent.run(prompt)

    # Convert the response to a string.
    return response.__str__()