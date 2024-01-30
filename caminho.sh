# Verificar se o ambiente conda já existe
if ! conda env list | grep -q "caminho_minimo"
then
    echo "Criando ambiente conda 'caminho_minimo'..."
    conda create --name caminho_minimo
    conda activate caminho_minimo

    # Instalar as bibliotecas necessárias
    echo "Instalando bibliotecas necessárias..."
    conda install -y -c conda-forge networkx pyvis numpy
fi

# Ativar o ambiente conda
echo "Ativando ambiente conda 'caminho_minimo'..."
conda activate caminho_minimo

# Executar o código Python
echo "Executando caminho_minimo.py..."
python3 caminho_minimo.py
