import cors from "cors";
import express from "express";
import accountRoutes from "./routes/accounts.js";

const app = express();
app.use(cors());
app.use(express.json());

app.use("/api/accounts", accountRoutes);

const PORT = 3001;
app.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`);
});
