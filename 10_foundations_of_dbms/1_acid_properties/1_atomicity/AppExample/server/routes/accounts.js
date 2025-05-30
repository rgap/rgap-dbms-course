import { PrismaClient } from "@prisma/client";
import express from "express";

const prisma = new PrismaClient();
const router = express.Router();

// ✅ Uppercase "A" matches model name in schema.prisma
router.get("/", async (_, res) => {
  const accounts = await prisma.Account.findMany();
  res.json(accounts);
});

router.post("/transfer", async (req, res) => {
  const { from, to, amount } = req.body;

  try {
    await prisma.$transaction([
      prisma.Account.update({
        where: { name: from },
        data: { balance: { decrement: amount } },
      }),
      prisma.Account.update({
        where: { name: to },
        data: { balance: { increment: amount } },
      }),
    ]);

    res.json({ success: true });
  } catch (err) {
    res.status(400).json({ success: false, message: err.message });
  }
});

export default router;
