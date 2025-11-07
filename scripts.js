// Chart Data
const expenseData = [
    { label: 'Salário', value: 3000, percentage: '56.3%' },
    { label: 'Custo de vida', value: 600, percentage: '11.3%' },
    { label: 'Gastos Presumidos', value: 560, percentage: '10.5%' },
    { label: 'Investimento', value: 500, percentage: '9.4%' },
    { label: 'Credito', value: 377, percentage: '7.1%' },
    { label: 'Assinatura', value: 214, percentage: '4.0%' },
    { label: 'Imposto', value: 80, percentage: '1.5%' }
];

// Chart Rendering
function renderChart() {
    const chart = document.getElementById('expenseChart');
    chart.innerHTML = '';
    const maxValue = Math.max(...expenseData.map(item => item.value));
    
    expenseData.forEach(item => {
        const barHeight = (item.value / maxValue) * 100;
        const bar = document.createElement('div');
        bar.className = 'bar';
        bar.style.height = `${barHeight}%`;
        bar.innerHTML = `
            <div class="bar-label">
                <div>${item.label}</div>
                <div style="font-weight: bold; color: var(--accent);">${item.percentage}</div>
            </div>
        `;
        chart.appendChild(bar);
    });
}

// Action Functions
function gerarNF() {
    alert('Função: Gerar Nota Fiscal\nIntegração com API de emissão de NF-e para MEI');
}

function importarExtrato() {
    alert('Função: Importar Extrato\nProcessamento automático de CSV/PDF de extratos bancários');
}

function classificarTransacoes() {
    alert('Função: Classificar Transações\nClassificação automática de receitas e despesas por categoria');
}

function gerarRelatorio() {
    alert('Função: Gerar Relatório\nGera relatório mensal em PDF/Excel com gráficos e análises');
}

function enviarAlertas() {
    alert('Função: Enviar Alertas\nEnvia alertas por e-mail/WhatsApp sobre pagamentos e obrigações');
}

function adicionarTransacao() {
    const type = document.getElementById('transactionType').value;
    const value = document.getElementById('transactionValue').value;
    const category = document.getElementById('transactionCategory').value;
    const date = document.getElementById('transactionDate').value;
    const description = document.getElementById('transactionDescription').value;
    
    if (value && date && description) {
        alert(`Transação adicionada:\nTipo: ${type}\nValor: R$ ${value}\nCategoria: ${category}\nData: ${date}\nDescrição: ${description}`);
        document.getElementById('transactionValue').value = '';
        document.getElementById('transactionDescription').value = '';
    } else {
        alert('Por favor, preencha todos os campos obrigatórios.');
    }
}

function processarArquivos() {
    alert('Processando arquivos...\nOs dados serão importados e categorizados automaticamente.');
}

// Initialization
document.addEventListener('DOMContentLoaded', function() {
    renderChart();
    document.getElementById('transactionDate').valueAsDate = new Date();
});