import streamlit as sp
import streamlit.components.v1 as components
HtmlFile = open("hello.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
# print(source_code)
components.html(source_code)  