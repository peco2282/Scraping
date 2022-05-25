import stweet as st


"""
def try_user_scrap():
    user_task = st.GetUsersTask(['shinjo_freedom'])
    output_json = st.JsonLineFileRawOutput('output_raw_user.jl')
    output_print = st.PrintRawOutput()
    st.GetUsersRunner(get_user_task=user_task, raw_data_outputs=[output_print, output_json]).run()
 
"""


def main():
    user = st.GetUsersTask(["peco_2282"])
    json = st.JsonLineFileRawOutput("output_raw_user.json")
    print = st.PrintRawOutput()
    st.GetUsersRunner(get_user_task=user, raw_data_outputs=[print, json]).run()


if __name__ == "__main__":
    main()
