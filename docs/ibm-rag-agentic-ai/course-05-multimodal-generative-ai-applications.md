# Course 5 - Build Multimodal Generative AI Applications

<span class="track-badge rag">IBM RAG & Agentic AI</span>

## What This Covers

This course covers multimodal AI systems that combine text, audio, image, and video. Local materials include readings on multimodal AI, computer vision, speech processing, text-to-speech, vision models, image/video generation, and labs for a meeting assistant, image captioning, DALL-E image generation, nutrition coaching, and style-finder retrieval.

## Core Ideas

- Multimodal systems accept or produce more than one media type.
- Speech-to-text turns audio into text that can be summarized or analyzed by an LLM.
- Text-to-speech turns generated text into audio output.
- Vision-language models can describe images, answer visual questions, or support image-grounded workflows.
- Multimodal retrieval can search images or products using text and visual features.
- Practical apps need clear media preprocessing and file handling.

## Important Formulas

Image similarity can use the same cosine similarity idea as text embeddings when images are embedded into vectors.

\[
\text{image similarity}(i_1,i_2) = \frac{v_1 \cdot v_2}{\|v_1\| \|v_2\|}
\]

Where:

- \(i_1\) and \(i_2\) are two images.
- \(v_1\) and \(v_2\) are their embedding vectors.
- Higher similarity means the images are closer in visual or semantic meaning.

Compression ratio is useful when thinking about audio/video processing cost.

\[
\text{compression ratio} = \frac{\text{original size}}{\text{compressed size}}
\]

Where:

- Original size is the raw or source media size.
- Compressed size is the stored or transmitted media size.

## Human-Readable Explanation

The meeting assistant lab demonstrates a common audio workflow: download or receive audio, transcribe it, summarize the transcript, and expose the result through Gradio. The important design point is that the LLM usually works on text after another model converts speech into text.

The image captioning and nutrition coach materials show the reverse pattern: an image becomes structured or descriptive text, and that text drives an application decision. The style finder extends retrieval beyond text by using multimodal similarity to match a visual or textual preference to relevant items.

## Key Code Patterns

Speech-to-text plus summarization:

```python
transcript = speech_to_text(audio_file)
summary = llm.invoke(f"Summarize this meeting:\n{transcript}")
```

Image-grounded application flow:

```python
description = vision_model.invoke(image)
recommendation = llm.invoke(f"Use this image description: {description}")
```

Gradio multimodal interface:

```python
demo = gr.Interface(fn=analyze_audio, inputs=gr.Audio(), outputs="text")
demo.launch()
```

## Common Mistakes

- Sending raw media to a text-only model.
- Ignoring file size, format, and preprocessing limits.
- Treating image captions as complete factual evidence.
- Building demos that depend on local paths instead of uploaded files.

## Takeaways

Course 5 shows how LLM applications become richer when other models convert images, audio, or video into usable context or generated media.
