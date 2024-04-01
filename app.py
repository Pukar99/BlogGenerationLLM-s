import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function To get response from LLAma 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    ### LLama2 model
    llm=CTransformers(model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template
    template = """
    Write a blog for {blog_style} job profile on the topic of "{input_text}" within {no_words} words.
    """
    
    prompt = PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    
    ## Generate the response from the LLama 2 model
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    return response

def main():
    st.set_page_config(page_title="📝 AI Blog Generator",
                    page_icon='🤖',
                    layout='wide',
                    initial_sidebar_state='expanded')

    st.title("📝 AI Blog Generator")

    input_text = st.text_input("🔍 Enter the Blog Topic")

    ## creating two more columns for additional 2 fields
    col1, col2 = st.columns([3,2])

    with col1:
        no_words = st.text_input('✍️ No. of Words', value="500")
    with col2:
        blog_style = st.selectbox('🖋️ Writing Style',
                                ('Professional', 'Casual', 'Academic'), index=0)
    
    submit = st.button("🚀 Generate Blog")

    ## Final response
    if submit:
        generated_blog = getLLamaresponse(input_text, no_words, blog_style)
        
        st.subheader("📝 Generated Blog:")
        st.markdown(generated_blog, unsafe_allow_html=True)

        # Enhancements:
        # 1. Allow user interaction to modify the generated blog
        st.subheader("✏️ Modify Blog:")
        modified_blog = st.text_area("✏️ Edit the Generated Blog", value=generated_blog, height=200)

        # 2. Add social sharing buttons
        st.subheader("🌐 Share Blog:")
        if st.button("Twitter 🐦"):
            # Code to share the blog on Twitter
            pass
        if st.button("Facebook 📘"):
            # Code to share the blog on Facebook
            pass

if __name__ == "__main__":
    main()
