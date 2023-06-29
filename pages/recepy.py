import streamlit as st

def show_recipe():
    st.title("Simon Fish Recipe")
    st.header("Ingredients:")
    st.markdown("- 500g white fish fillets")
    st.markdown("- 2 tablespoons olive oil")
    st.markdown("- 1 lemon, juiced")
    st.markdown("- Salt and pepper to taste")
    st.markdown("- Fresh parsley for garnish")
    
    st.header("Instructions:")
    st.markdown("1. Preheat the oven to 180°C (350°F).")
    st.markdown("2. Place the fish fillets in a baking dish.")
    st.markdown("3. Drizzle the olive oil and lemon juice over the fish.")
    st.markdown("4. Season with salt and pepper to taste.")
    st.markdown("5. Bake in the preheated oven for 20-25 minutes or until the fish is cooked through and flakes easily with a fork.")
    st.markdown("6. Garnish with fresh parsley before serving.")
    st.markdown("7. Enjoy your delicious Simon Fish!")
    
    st.header("Tips:")
    st.markdown("- You can use any white fish fillets such as cod, haddock, or tilapia.")
    st.markdown("- Serve with steamed vegetables or a side salad for a complete meal.")
    
# Display the recipe page
show_recipe()
