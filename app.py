import streamlit as st

# Logo
st.image("logo.jpg")

# Tiêu đề
st.title("APP TÍNH THUẾ THU NHẬP CÁ NHÂN")

st.write("Nhập thu nhập tính thuế để tính số thuế phải nộp theo biểu thuế lũy tiến từng phần.")

# Nhập dữ liệu
income = st.number_input(
    "Nhập thu nhập tính thuế (triệu đồng/tháng)",
    min_value=0.0,
    value=20.0
)

# Hàm tính thuế
def tinh_thue(tn):
    tax = 0

    if tn <= 5:
        tax = tn * 0.05

    elif tn <= 10:
        tax = 5 * 0.05 + (tn - 5) * 0.10

    elif tn <= 18:
        tax = 5 * 0.05 + 5 * 0.10 + (tn - 10) * 0.15

    elif tn <= 32:
        tax = 5 * 0.05 + 5 * 0.10 + 8 * 0.15 + (tn - 18) * 0.20

    elif tn <= 52:
        tax = (
            5 * 0.05 +
            5 * 0.10 +
            8 * 0.15 +
            14 * 0.20 +
            (tn - 32) * 0.25
        )

    elif tn <= 80:
        tax = (
            5 * 0.05 +
            5 * 0.10 +
            8 * 0.15 +
            14 * 0.20 +
            20 * 0.25 +
            (tn - 52) * 0.30
        )

    else:
        tax = (
            5 * 0.05 +
            5 * 0.10 +
            8 * 0.15 +
            14 * 0.20 +
            20 * 0.25 +
            28 * 0.30 +
            (tn - 80) * 0.35
        )

    return tax

# Nút tính
if st.button("Tính thuế"):
    tax = tinh_thue(income)
    remain = income - tax

    st.subheader("Kết quả")

    st.success(f"Thuế thu nhập cá nhân phải nộp: {tax:,.2f} triệu đồng")

    st.info(f"Thu nhập còn lại sau khi nộp thuế: {remain:,.2f} triệu đồng")
