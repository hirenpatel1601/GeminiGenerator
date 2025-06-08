import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
import re 
from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled,NoTranscriptFound 

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_summery(text):
    model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")
    prompt = f"Summarize The following youtube video transcript concisely : {text} create a summary that is easy to understand and captures the main points of the video."
    response = model.generate_content([prompt])
    return response.text

def Extract_youtubevideo_id(url):
    '''Extracts the YouTube video ID from a given URL.'''

    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern,url)
    if match:
        return match.group(1)
    return None
st.title("The Professor's Academy Assistant")
st.header("Give Me Link Of Youtube Video i will Summarize YouTube Video For You!")
url = st.text_input("Enter the YouTube video URL:", key="url")
submitbtn = st.button("Get Summary")

if submitbtn and url.strip():
    video_id = Extract_youtubevideo_id(url)
    if not video_id:
        st.error("Invalid YouTube URL. Please enter a valid URL.")
    else:
        try:
            # Fetch transcript
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            #print(transcript_list)
            if not transcript_list:
                st.error("No transcript found for this video.")
                raise NoTranscriptFound("No transcript available for this video.")
            transcript_text = " ".join(
                [item['text'] for item in transcript_list]
            )
            #st.header(transcript_text)    
            st.info("Transcript successfully fetched. Generating summary...")
            summary = get_gemini_summery(transcript_text)
            st.subheader("Video Summary")
            st.write(summary)
            st.subheader("Notes From Video")
            
            notes = get_gemini_summery(transcript_text + " create notes from this video for study purpose.")
            st.write(notes)

        except (TranscriptsDisabled, NoTranscriptFound):
            st.error("Transcript not available for this video.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")


# import streamlit as st
# import os
# from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
# import google.generativeai as genai
# from dotenv import load_dotenv
# import re

# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_summary(text):
#     model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
#     prompt = f"Summarize the following YouTube video transcript concisely:\n\n{text}"
#     response = model.generate_content([prompt])
#     return response.text

# def extract_video_id(url):
#     """
#     Extract YouTube video ID from URL.
#     """
#     # Common YouTube URL formats:
#     # https://www.youtube.com/watch?v=VIDEO_ID
#     # https://youtu.be/VIDEO_ID
#     pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
#     match = re.search(pattern, url)
#     if match:
#         return match.group(1)
#     return None

# st.set_page_config(page_title="YouTube Video Summarizer")

# st.title("YouTube Video Summarizer with Gemini AI")

# option = st.radio("Select input type:", ("YouTube URL", "Upload Video File"))

# if option == "YouTube URL":
#     youtube_url = st.text_input("Enter YouTube video URL:")
#     if st.button("Summarize Video") and youtube_url.strip():
#         video_id = extract_video_id(youtube_url)
#         if not video_id:
#             st.error("Invalid YouTube URL. Please enter a correct video link.")
#         else:
#             try:
#                 # Fetch transcript
#                 transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
#                 transcript_text = " ".join([item['text'] for item in transcript_list])
                
#                 st.info("Transcript successfully fetched. Generating summary...")
#                 summary = get_gemini_summary(transcript_text)
#                 st.subheader("Video Summary")
#                 st.write(summary)

#             except TranscriptsDisabled:
#                 st.error("Transcripts are disabled for this video.")
#             except NoTranscriptFound:
#                 st.error("No transcript found for this video.")
#             except Exception as e:
#                 st.error(f"Error fetching transcript: {e}")

# elif option == "Upload Video File":
#     uploaded_file = st.file_uploader("Upload video file (MP4, etc.)")
#     if uploaded_file:
#         st.warning("Uploaded video summarization is not yet supported.")
#         st.info("To summarize a video, please provide a YouTube URL with transcripts.")