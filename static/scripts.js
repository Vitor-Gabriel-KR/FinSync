// Função para abrir/fechar os cards individualmente
document.addEventListener('DOMContentLoaded', function() {
    const nfeItems = document.querySelectorAll('.nfe-item');
    
    nfeItems.forEach(item => {
        item.addEventListener('click', function(e) {
            // Impedir que o clique no status dispare o toggle do card
            if (e.target.classList.contains('nfe-status')) return;
            
            if (this.classList.contains('expanded')) {
                this.classList.remove('expanded');
            } else {
                nfeItems.forEach(otherItem => otherItem.classList.remove('expanded'));
                this.classList.add('expanded');
            }
        });
    });

    // Função para mudar o estado do status
    const estados = [
        { texto: "Pendente", classe: "status-pending" },
        { texto: "Emitida", classe: "status-paid" },
        { texto: "Atrasada", classe: "status-overdue" }
    ];

    const statusElements = document.querySelectorAll(".nfe-status");

    statusElements.forEach(statusEl => {
        statusEl.style.cursor = "pointer";

        statusEl.addEventListener("click", async function(e) {
            e.stopPropagation(); // Impedir que o clique propague para o card
            
            const atual = statusEl.textContent.trim();
            let idx = estados.findIndex(e => e.texto === atual);
            if (idx === -1) idx = 0;

            const proximo = estados[(idx + 1) % estados.length];

            // Remove as classes antigas
            statusEl.classList.remove("status-pending", "status-paid", "status-overdue");

            // Adiciona a nova
            statusEl.classList.add(proximo.classe);
            statusEl.textContent = proximo.texto;

            // Captura o número da NF
            const nfItem = statusEl.closest(".nfe-item");
            const numeroNF = nfItem.querySelector(".nfe-details div:nth-child(3)")?.textContent.replace("Número NF:", "").trim();

            console.log(`🟡 Atualizando status da NF ${numeroNF} → ${proximo.texto}`);

            // Atualiza o status no banco via Flask
            try {
                const response = await fetch("/atualizar_status", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        numero_nf: numeroNF,
                        status: proximo.texto
                    })
                });

                const result = await response.json();

                if (result.success) {
                    console.log("✅ Status atualizado no banco com sucesso!");
                } else {
                    console.error("❌ Erro ao atualizar status:", result.error);
                    alert("Erro ao atualizar status no banco: " + result.error);
                }
            } catch (err) {
                console.error("❌ Falha na requisição:", err);
                alert("Falha ao conectar ao servidor.");
            }
        });
    });
});

// ======== CHART DATA ======== //
const expenseData = [
    { label: 'Salário', value: 3000, percentage: '56.3%' },
    { label: 'Custo de vida', value: 600, percentage: '11.3%' },
    { label: 'Gastos Presumidos', value: 560, percentage: '10.5%' },
    { label: 'Investimento', value: 500, percentage: '9.4%' },
    { label: 'Credito', value: 377, percentage: '7.1%' },
    { label: 'Assinatura', value: 214, percentage: '4.0%' },
    { label: 'Imposto', value: 80, percentage: '1.5%' }
];

// ======== CHART RENDERING ======== //
function renderChart() {
    const chart = document.getElementById('expenseChart');
    if (!chart) return;
    
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

// ======== AÇÕES ======== //
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

document.addEventListener('DOMContentLoaded', function() {
    renderChart();
    const transactionDate = document.getElementById('transactionDate');
    if (transactionDate) {
        transactionDate.valueAsDate = new Date();
    }
});
