// app.js
import * as tf from "@tensorflow/tfjs-node";
import * as tflite from "@tensorflow/tfjs-tflite";
import { AutoTokenizer } from "@xenova/transformers";

// 1. 모델 및 토크나이저 로드
const MODEL_PATH = "file://./distilbert_qa.tflite";
const TOKENIZER_PATH = "./distilbert_qa_tf";

const model = await tflite.loadTFLiteModel(MODEL_PATH);
const tokenizer = await AutoTokenizer.from_pretrained(TOKENIZER_PATH);

console.log("TFLite 모델 로드");

// 2. 입력 텍스트
const context = "TensorFlow Lite enables on-device machine learning.";
const question = "What does TensorFlow Lite enable?";

// 3. 토크나이징
const encoded = await tokenizer(question, context);
const input_ids = tf.tensor([encoded.input_ids]);
const attention_mask = tf.tensor([encoded.attention_mask]);

// 4. TFLite 모델 추론
const outputs = model.predict([input_ids, attention_mask]);

// 5. 출력 텐서 확인
const start_logits = outputs[0].arraySync()[0];
const end_logits = outputs[1].arraySync()[0];
const start_idx = start_logits.indexOf(Math.max(...start_logits));
const end_idx = end_logits.indexOf(Math.max(...end_logits));

// 6. 결과 디코딩
const answer = tokenizer.decode(encoded.input_ids.slice(start_idx, end_idx + 1));
console.log("Answer:", answer);
