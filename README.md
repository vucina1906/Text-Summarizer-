The goal of this project is to leverage the power of transfer learning to build a model capable of summarizing dialogues.

For those of you who may not be aware, transfer learning is a machine learning technique in which we use a pre-trained model—that is already knowledgeable in a wide domain—and tailor its expertise for a specific task by training it in a specific dataset we might have. This process may also be referred to as fine-tuning.

The task at hand is Text Summarization. From the documentation of the Hugging Face Transformers library, summarization can be described as the creation of a shorter version of a document or an article that captures all the important information. In this case, we are going to summarize dialogues by using a dataset containing chat texts. We are going to use the SamSum Dataset, which contains three csv files for training, testing, and validation. All these files are structured into a specific id, a dialogue, and a summary. The SamSum dataset consists of chat texts, which is ideal for the summarization of dialogues.

In this case, I have decided to use the BART architecture, more specifically, I am going to fine-tune a version of BART that has been already trained to perform text summarization of news articles, which is the facebook/bart-large-xsum version. The goal of our model is to produce a short sentence describing the content of a dialogue, while maintaining all the important information within that dialogue.

