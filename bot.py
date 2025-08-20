from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler
import logging
import os

# إعداد التسجيل
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# التوكن الخاص بك
TOKEN = "8362652916:AAFOdF5lpN9XHraA4VcCH6qHrKlQVzL2hVo"

# بيانات المستخدمين
users = {}

# لوحة المفاتيح الرئيسية
def main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💳 تعبئة الرصيد", callback_data='deposit')],
        [InlineKeyboardButton("📤 سحب الأرباح", callback_data='withdraw')],
        [InlineKeyboardButton("📊 حسابي", callback_data='account')],
        [InlineKeyboardButton("🎯 المهام اليومية", callback_data='tasks')],
        [InlineKeyboardButton("👥 دعوة الأصدقاء", callback_data='referral')],
        [InlineKeyboardButton("⭐ خطط VIP", callback_data='vip')],
        [InlineKeyboardButton("📋 السجلات المالية", callback_data='records')],
        [InlineKeyboardButton("🌐 فتح التطبيق", web_app={"url": "https://username.github.io/bks-cincos-bot"})]
    ])

async def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id not in users:
        users[user_id] = {
            'balance': 0.0,
            'vip_level': 0,
            'referral_code': str(user_id),
            'referred_by': None,
            'daily_tasks': False
        }
    
    welcome_message = """
🎊 *مرحباً بك في BKS Cincos* 🎊

🤝 *شركاؤنا الاستراتيجيون*:
🏢 Huawei • 🏢 Alibaba • 🏢 Tencent
🏢 Xiaomi • 🏢 BYD • 🏢 China Mobile

💰 *رصيدك الحالي:* 0.00 USDT
⭐ *مستوى VIP:* VIP0

📈 *استثمر وانمو مع أكبر الشركات الصينية*
    """
    
    await update.message.reply_text(
        welcome_message,
        parse_mode='Markdown',
        reply_markup=main_keyboard()
    )

async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'deposit':
        await deposit_handler(query)
    elif query.data == 'withdraw':
        await withdraw_handler(query)
    elif query.data == 'vip':
        await vip_handler(query)

async def deposit_handler(query):
    deposit_message = """
💳 *تعبئة الرصيد - BKS Cincos*

🌐 *العنوان:* TADKZeL7ZkZyP5qfsfTV4voamnbJQh4VU

📝 *تعليمات الإيداع:*
1. انسخ العنوان أعلاه
2. أرسل USDT فقط (شبكة TRC20)
3. سيصل الرصيد خلال 1-3 دقائق

⚠ *تحذير:* لا ترسل أي عملة أخرى غير USDT
    """
    
    await query.edit_message_text(
        deposit_message,
        parse_mode='Markdown',
        reply_markup=main_keyboard()
    )

async def vip_handler(query):
    vip_message = """
⭐ *خطط الاستثمار VIP - BKS Cincos*

📊 *VIP1 (1.00 USDT):*
• ربح يومي: 1.00 USDT
• إجمالي الأرباح: 60.00 USDT

📊 *VIP2 (16.00 USDT):*
• ربح يومي: 10.00 USDT
• إجمالي الأرباح: 600.00 USDT

📊 *VIP3 (116.00 USDT):*
• ربح يومي: 80.00 USDT
• إجمالي الأرباح: 7,200.00 USDT

🚀 *ارفع مستوى استثمارك وزد أرباحك!*
    """
    
    await query.edit_message_text(
        vip_message,
        parse_mode='Markdown',
        reply_markup=main_keyboard()
    )

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.run_polling()

if __name__ == "__main__":
    main()
