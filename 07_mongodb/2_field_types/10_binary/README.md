### Binary Fields

Binary fields store arbitrary binary data such as files, encrypted content, or compressed blobs. They use BSON's native binary type.

📄 This example encodes binary file content in base64. MongoDB stores it using the BSON Binary type with an optional subtype.

🧱 **Example Fields**:

- `_id`: A string identifier.
- `filename`: A string name of the uploaded file.
- `data`: A base64-encoded binary buffer with a subtype.

📌 **Use Cases**:

- Storing images, PDFs, audio files, or videos directly in the database.
- Handling encrypted values, hash results, or binary payloads.
- Representing compact formats such as Protocol Buffers.

✅ **Advantages**:

- Efficient for handling non-textual or compressed data.
- Can be processed securely in binary form.
- Subtypes allow for organization of binary content (e.g., UUID, encrypted).

🚫 **Limitations**:

- Base64-encoded data is bulky when exported to JSON.
- Not ideal for large files (GridFS is better for streaming large content).
- Retrieval and display require decoding logic on the client side.
