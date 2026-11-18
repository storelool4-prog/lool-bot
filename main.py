import re, os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""

    product = "ماسي"
    if "بلور" in text:
        product = "بلورة"
    elif "ماس" in text:
        product = "ماسي"

    m_id = re.search(r"PlayerId:\s*(\d+)", text)
    m_qty = re.search(r"الكمية:\s*([\d,]+)", text)

    if not m_id or not m_qty:
        return

    player_id = m_id.group(1)
    amount = m_qty.group(1).replace(",", "")

    await update.message.reply_text(f"⏳ جاري الشحن... {amount} {product} لـ {player_id}")
    await update.message.reply_text(f"✅ تم استلام الطلب - {amount} {product} لـ {player_id} - جاري ربطه مع ihago")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))
app.run_polling()
