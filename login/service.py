import streamlit as st
import time
from api.service import Auth


def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(
        username=username,
        password=password,
    )
    if response.get('error'):
        st.toast(f':black[Opa, verifique usuário e senha!]', icon="⚠️")
        st.markdown(
            """
                <style>
                        div[data-testid=stToast] {
                            padding: 15px 25px 15px 10px;
                            width: 20%;
                            background-color: #FF6347;
                            color: #000000;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                        }
                </style>
            """,
            unsafe_allow_html=True
        )

        time.sleep(.5)

    else:                # | variable is token
        st.session_state.token = response.get('access')
        st.rerun()


def logout():
    for key in st.session_state.key():
        del st.session_state[key]
    st.rerun()
