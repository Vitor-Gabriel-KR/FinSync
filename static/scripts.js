// Função para abrir/fechar os cards individualmente
document.addEventListener('DOMContentLoaded', function() {
    const nfeItems = document.querySelectorAll('.nfe-item');
    
    nfeItems.forEach(item => {
        item.addEventListener('click', function(e) {
            if (e.target.classList.contains('nfe-status')) return;
            
            if (this.classList.contains('expanded')) {
                this.classList.remove('expanded');
            } else {
                nfeItems.forEach(otherItem => otherItem.classList.remove('expanded'));
                this.classList.add('expanded');
            }
        });
    });

    const estados = [
        { texto: "Pendente", classe: "status-pending" },
        { texto: "Emitida", classe: "status-paid" },
        { texto: "Atrasada", classe: "status-overdue" }
    ];

    const statusElements = document.querySelectorAll(".nfe-status");

    statusElements.forEach(statusEl => {
        statusEl.style.cursor = "pointer";

        statusEl.addEventListener("click", async function(e) {
            e.stopPropagation();
            
            const atual = statusEl.textContent.trim();
            let idx = estados.findIndex(e => e.texto === atual);
            if (idx === -1) idx = 0;

            const proximo = estados[(idx + 1) % estados.length];

            statusEl.classList.remove("status-pending", "status-paid", "status-overdue");
            statusEl.classList.add(proximo.classe);
            statusEl.textContent = proximo.texto;

            const nfItem = statusEl.closest(".nfe-item");
            const numeroNF = nfItem.querySelector(".nfe-details div:nth-child(3)")?.textContent.replace("Número NF:", "").trim();

            console.log(`Atualizando status da NF ${numeroNF} → ${proximo.texto}`);

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
                    console.log("Status atualizado no banco com sucesso!");
                } else {
                    console.error("Erro ao atualizar status:", result.error);
                    alert("Erro ao atualizar status no banco: " + result.error);
                }
            } catch (err) {
                console.error("Falha na requisição:", err);
                alert("Falha ao conectar ao servidor.");
            }
        });
    });

    renderChart();
    const transactionDate = document.getElementById('transactionDate');
    if (transactionDate) {
        const today = new Date();
        transactionDate.value = today.toISOString().split('T')[0];
    }
});

const expenseData = [
    { label: 'Salário', value: 3000, percentage: '56.3%' },
    { label: 'Custo de vida', value: 600, percentage: '11.3%' },
    { label: 'Gastos Presumidos', value: 560, percentage: '10.5%' },
    { label: 'Investimento', value: 500, percentage: '9.4%' },
    { label: 'Credito', value: 377, percentage: '7.1%' },
    { label: 'Assinatura', value: 214, percentage: '4.0%' },
    { label: 'Imposto', value: 80, percentage: '1.5%' }
];

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

// Modal de Evento
let currentEventId = null;

function openEventModal(eventId) {
    currentEventId = eventId;
    
    fetch(`/get_evento/${eventId}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const evento = data.evento;
                
                document.getElementById('eventId').value = evento.id;
                document.getElementById('eventName').value = evento.nome;
                document.getElementById('eventValue').value = evento.valor;
                document.getElementById('eventPaid').value = evento.pago.toString();
                document.getElementById('eventRecurrent').value = evento.recorrente.toString();
                document.getElementById('eventActive').value = evento.ativo.toString();
                
                // Atualiza o título do modal para incluir o status
                const modalTitle = document.getElementById('modalTitle');
                if (!evento.ativo) {
                    modalTitle.innerHTML = '📝 Editar Evento <span style="color: #666; font-size: 0.8em;">(Inativo)</span>';
                } else {
                    modalTitle.innerHTML = '📝 Editar Evento';
                }
                
                document.getElementById('eventModal').style.display = 'block';
            } else {
                alert('Erro ao carregar evento: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert('Erro ao carregar evento');
        });
}

function closeEventModal() {
    document.getElementById('eventModal').style.display = 'none';
    currentEventId = null;
}

// Fechar modal ao clicar fora
document.getElementById('eventModal').addEventListener('click', function(e) {
    if (e.target === this) {
        closeEventModal();
    }
});

// Submeter formulário de evento
document.getElementById('eventForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = {
        id: document.getElementById('eventId').value,
        nome: document.getElementById('eventName').value,
        valor: parseFloat(document.getElementById('eventValue').value),
        pago: document.getElementById('eventPaid').value === 'true',
        recorrente: document.getElementById('eventRecurrent').value === 'true',
        ativo: document.getElementById('eventActive').value === 'true'
    };
    
    fetch('/atualizar_evento', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            closeEventModal();
            location.reload();
        } else {
            alert('Erro ao atualizar evento: ' + data.error);
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao atualizar evento');
    });
});

function animateCalendar(direction) {
    const container = document.getElementById('calendar-container');
    if (!container) return;
    
    container.style.animation = `slideOut${direction === 'left' ? 'Left' : 'Right'} 0.3s ease`;
    
    setTimeout(() => {
        container.style.animation = `slideIn${direction === 'left' ? 'Right' : 'Left'} 0.3s ease`;
    }, 300);
}