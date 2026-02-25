import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

df = pd.read_csv('anime_data_eda.csv') # Usando o nome do arquivo que salvamos antes

# Definição das colunas (mesma lógica do seu código)
top_genres = ['mystery', 'suspense', 'sports', 'drama', 'slice_of_life', 'romance', 
              'adventure', 'supernatural', 'gourmet', 'action', 'fantasy', 'comedy', 'sci-fi']
top_themes = ['theme_iyashikei', 'theme_childcare', 'theme_gag_humor', 'theme_organized_crime', 
              'theme_adult_cast', 'theme_visual_arts', 'theme_love_status_quo', 'theme_love_polygon', 
              'theme_performing_arts', 'theme_combat_sports', 'theme_urban_fantasy', 'theme_cgdct', 
              'theme_team_sports', 'theme_otaku_culture', 'theme_showbiz', 'theme_historical', 
              'theme_time_travel', 'theme_racing', 'theme_delinquents', 'theme_detective', 
              'theme_medical', 'theme_military', 'theme_samurai', 'theme_school']

# 2. Engenharia de Variáveis (Feature Engineering)
df['log_favorites'] = np.log1p(df['favorites'])
df['log_episodes'] = np.log1p(df['episodes']) # Adicionado para evitar erro no X

# Criar dummies para Rating
rating_dummies = pd.get_dummies(df['rating'], prefix='rating', drop_first=True)

# 3. Preparação do X e y
X = pd.concat([
    df[['log_episodes', 'log_favorites']], 
    df[top_genres], 
    df[top_themes],
    rating_dummies
], axis=1)
y = df['score']

# 4. Dividir Treino e Teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Treinar o Modelo Linear
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# 6. Avaliação
y_pred_lr = lr_model.predict(X_test)
mae_lr = mean_absolute_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

print(f"Linear Regression MAE: {mae_lr:.3f}")
print(f"Linear Regression R²: {r2_lr:.3f}")

# 7. Pesos (Drivers de Score)
coeff_df = pd.DataFrame({
    'Feature': X.columns,
    'Weight': lr_model.coef_
}).sort_values(by='Weight', ascending=False)

print("\n--- Principais Influenciadores Positivos ---")
print(coeff_df.head(5))

# 8. Visualização de Resíduos (Erro do Modelo Linear)
residuals = y_test - y_pred_lr # Corrigido para y_pred_lr

plt.figure(figsize=(10, 6))
sns.histplot(residuals, kde=True, color='blue')
plt.axvline(0, color='red', linestyle='--')
plt.title('Distribuição de Resíduos (Erros) - Regressão Linear')
plt.xlabel('Erro de Predição (Real - Previsto)')
plt.show()

# 9. Salvar e Testar o Modelo
with open('anime_linear_model.pkl', 'wb') as file:
    pickle.dump(lr_model, file) # Salvando o modelo linear

print("\nModelo salvo com sucesso!")

# Teste rápido
sample_anime = X_test.iloc[[0]] 
with open('anime_linear_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
    
prediction = loaded_model.predict(sample_anime)
print(f"Predição: {prediction[0]:.2f} | Real: {y_test.iloc[0]:.2f}")