import streamlit as st
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

    # Write the response to the Streamlit app.
    st.write(response)

