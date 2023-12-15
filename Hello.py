# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import requests

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello streamlit",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")

    df = pd.DataFrame({
      'first column': [1, 2, 3, 4],
      'second column': [10, 20, 30, 40],
      'third col': ['zb', 'lk', 'ga', 'mengr']
    })

    df


    st.sidebar.success("Select a demo above.")



if __name__ == "__main__":
    run()
