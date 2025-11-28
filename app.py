import streamlit as st

# -----------------------------
# FAQ Database
# -----------------------------
faqs = {
    "pricing": "Our pricing starts at ₹499 per month for the basic plan. Discounts available for annual subscriptions.",
    "refund": "Refunds are processed within 5–7 working days after approval.",
    "delivery": "Delivery usually takes 3–5 business days for metro cities and 5–7 days for other regions.",
    "features": "Our product includes AI support, analytics dashboard, cloud backup, and 24/7 monitoring.",
    "support": "You can contact support via email support@example.com or call +91-98765-43210.",
    "payment methods": "We accept UPI, credit/debit cards, net banking, and EMI options.",
    "cancel order": "To cancel an order, go to My Orders → Select Order → Cancel before shipping.",
    "track order": "Track your order using the tracking ID sent to your email/SMS.",
    "warranty": "All products come with a 1-year standard warranty.",
    "technical issue": "Restart the device and check internet. If the issue continues, contact support.",
    "account reset": "Reset your account password using the 'Forgot Password' option on login page.",
    "free trial": "We offer a 7-day free trial for all new users.",
    "bulk order": "For bulk purchases, email sales@example.com for special pricing.",
    "international shipping": "Yes, we ship internationally. Delivery times vary by location.",
    "return policy": "Items can be returned within 10 days if unused and in original condition.",
    "invoice": "Invoices are automatically emailed after a successful order.",
    "lost package": "If your package is lost, we replace it or issue a full refund.",
    "slow app": "Clear cache or update the app to the latest version.",
    "account blocked": "Account blocked due to unusual activity; contact support.",
    "data privacy": "We follow strict data protection laws to secure your information.",
    "newsletter": "Subscribe to our newsletter for updates and offers.",
    "product demo": "Request a free product demo via video call.",
    "chat hours": "Live chat available from 9 AM to 9 PM IST.",
    "server down": "Technical team is working if servers are down.",
    "reschedule delivery": "Reschedule via courier partner's tracking page.",
    "product authenticity": "All products are 100% original from verified suppliers.",
    "loyalty points": "Earn points on every purchase; redeemable for discounts.",
    "billing issues": "Contact billing support for invoice or payment issues.",
    "promo codes": "Apply promo codes at checkout for discounts.",
    "priority support": "Available for premium subscribers with dedicated agents.",
    "password change": "Change your password via Account → Security → Change Password.",
    "feature request": "Submit feature requests through Feedback → Suggest Feature.",
    "subscription cancel": "Cancel your subscription from Dashboard → Manage Plan.",
}

# -----------------------------
# Functions
# -----------------------------
def find_answer(query):
    query = query.lower()
    for keyword, answer in faqs.items():
        if keyword in query:
            return answer
    return None

def escalate_query(query):
    return (
        "⚠️ This query seems complex.\n"
        "I am escalating it to a human agent.\n"
        "Our team will contact you within 24 hours.\n"
        f"Your message: {query}"
    )

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Support Assistant", page_icon="🤖")

st.title("🤖 Support Assistant")
st.write("Ask any question about our products or services. Type 'exit' to end the chat.")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:")

if user_input:
    if user_input.lower() == "exit":
        st.session_state.history.append(("System", "Thank you! Have a great day 😊"))
    else:
        answer = find_answer(user_input)
        if answer:
            st.session_state.history.append(("Assistant", answer))
        else:
            st.session_state.history.append(("Assistant", escalate_query(user_input)))
        st.session_state.history.append(("You", user_input))

# Display chat history
for sender, message in st.session_state.history:
    if sender == "You":
        st.markdown(f"<div style='text-align: right; color: blue;'><b>You:</b> {message}</div>", unsafe_allow_html=True)
    elif sender == "Assistant":
        st.markdown(f"<div style='text-align: left; color: green;'><b>Assistant:</b> {message}</div>", unsafe_allow_html=True)
    else:  # System messages
        st.markdown(f"<div style='text-align: center; color: gray;'><i>{message}</i></div>", unsafe_allow_html=True)
