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
    
    const nfEmissao = document.getElementById('nfEmissao');
    if (nfEmissao) {
        const today = new Date();
        nfEmissao.value = today.toISOString().split('T')[0];
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

function showTab(tabName) {
    document.querySelectorAll('.tab-button').forEach(btn => {
        btn.classList.remove('active');
    });
    
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    
    event.target.classList.add('active');
    document.getElementById(tabName + '-tab').classList.add('active');
}

function adicionarTransacao() {
    const data = {
        data: document.getElementById('transactionDate').value,
        categoria: document.getElementById('transactionCategory').value,
        valor: document.getElementById('transactionValue').value,
        descricao: document.getElementById('transactionDescription').value,
        nome: document.getElementById('transactionName').value
    };

    if (!data.data || !data.categoria || !data.valor) {
        alert('Por favor, preencha Data, Categoria e Valor.');
        return;
    }

    fetch('/adicionar_transacao', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Transação adicionada com sucesso!');
            document.getElementById('transactionValue').value = '';
            document.getElementById('transactionDescription').value = '';
            document.getElementById('transactionName').value = '';
        } else {
            alert('Erro: ' + data.error);
        }
    })
    .catch(error => {
        alert('Erro de conexão: ' + error);
    });
}

function adicionarNotaFiscal() {
    const data = {
        numero_nf: document.getElementById('nfNumber').value,
        fornecedor: document.getElementById('nfFornecedor').value,
        valor: document.getElementById('nfValor').value,
        data_emissao: document.getElementById('nfEmissao').value,
        mes_referencia: document.getElementById('nfMesReferencia').value,
        status: document.getElementById('nfStatus').value,
        cliente: document.getElementById('nfFornecedor').value,
        contato: document.getElementById('nfContato').value,
        cnpj: document.getElementById('nfCNPJ').value
    };

    if (!data.numero_nf || !data.fornecedor || !data.valor) {
        alert('Por favor, preencha Número NF, Fornecedor e Valor.');
        return;
    }

    fetch('/adicionar_nota_fiscal', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Nota fiscal adicionada com sucesso!');
            document.getElementById('nfNumber').value = '';
            document.getElementById('nfFornecedor').value = '';
            document.getElementById('nfValor').value = '';
            document.getElementById('nfContato').value = '';
            document.getElementById('nfCNPJ').value = '';
        } else {
            alert('Erro: ' + data.error);
        }
    })
    .catch(error => {
        alert('Erro de conexão: ' + error);
    });
}

function adicionarPrevisaoMes() {
    const data = {
        mes_referencia: document.getElementById('previsaoMes').value,
        salario: document.getElementById('previsaoSalario').value,
        custo_vida: document.getElementById('previsaoCustoVida').value,
        gastos_presumidos: document.getElementById('previsaoGastos').value,
        investimento: document.getElementById('previsaoInvestimento').value,
        credito: document.getElementById('previsaoCredito').value,
        assinaturas: document.getElementById('previsaoAssinaturas').value,
        imposto: document.getElementById('previsaoImposto').value
    };

    if (!data.mes_referencia) {
        alert('Por favor, preencha o Mês de Referência.');
        return;
    }

    fetch('/adicionar_previsao_mes', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Previsão do mês adicionada com sucesso!');
            document.getElementById('previsaoMes').value = '';
            document.getElementById('previsaoSalario').value = '';
            document.getElementById('previsaoCustoVida').value = '';
            document.getElementById('previsaoGastos').value = '';
            document.getElementById('previsaoInvestimento').value = '';
            document.getElementById('previsaoCredito').value = '';
            document.getElementById('previsaoAssinaturas').value = '';
            document.getElementById('previsaoImposto').value = '';
        } else {
            alert('Erro: ' + data.error);
        }
    })
    .catch(error => {
        alert('Erro de conexão: ' + error);
    });
}

function processarArquivos() {
    alert('Processando arquivos...\nOs dados serão importados e categorizados automaticamente.');
}

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

document.getElementById('eventModal').addEventListener('click', function(e) {
    if (e.target === this) {
        closeEventModal();
    }
});

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