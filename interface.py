import streamlit as st
import pandas as pd
from agent import agent_query, generate_agent

st.title("HUMANIZE YOUR DATA!")

st.title("Make a conversation with your CSV files")

data = st.file_uploader("Upload a CSV")

query = st.text_area("Insert your query")

if st.button("Submit Query", type="primary"):
    # Create an agent from the CSV file.
    agent = generate_agent(data)

    # Query the agent.
    response = agent_query(agent=agent, query=query)

    # Decode the response.
    #response_dict = json.loads(response)

    # Write the response to the Streamlit app.
    st.write(response)
    # if "answer" in response_dict:
    #     st.write(response_dict['answer])

    # if "bar" in response_dict:
    #     data = response_dict["bar"]
    #     df = pd.DataFrame(data)
    #     df.set_index("columns", inplace=True)
    #     st.bar_chart(df)

    # if "line" in response_dict:
    #     data = response_dict["line"]
    #     df = pd.DataFrame(data)
    #     df.set_index("columns", inplace=True)
    #     st.line_chart(df)

    # if "table" in response_dict:
    #     data = response_dict["table"]
    #     df = pd.DataFrame(data["data"], columns=data["columns"])
    #     st.table(df)

