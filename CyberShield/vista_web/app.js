const rows = document.getElementById('processRows');
const events = document.getElementById('eventList');
let nextPid = 5100;
function addEvent(title, detail, color='blue-dot') {
  const now = new Date().toLocaleTimeString('es-CO', {hour12:false});
  const item = document.createElement('div');
  item.className = 'event';
  const dot = document.createElement('span'); dot.className = `event-dot ${color}`;
  const body = document.createElement('span');
  const b = document.createElement('b'); b.textContent = title;
  const small = document.createElement('small'); small.textContent = detail;
  body.append(b, small);
  const time = document.createElement('time'); time.textContent = now;
  item.append(dot, body, time); events.prepend(item);
}
document.getElementById('addProcess').addEventListener('click', () => {
  const pid = nextPid++;
  const name = `process_demo_${pid}`;
  const tr = document.createElement('tr');
  const values = [pid, name, 'Listo', '0.0%', '48 MB', 'Normal'];
  values.forEach((value, index) => {
    const td = document.createElement('td');
    if (index === 1) { const b = document.createElement('b'); b.textContent = value; td.append(b); }
    else if (index === 2) { const span = document.createElement('span'); span.className='status paused'; span.textContent=value; td.append(span); }
    else td.textContent = value;
    tr.append(td);
  });
  rows.append(tr);
  document.getElementById('processCount').textContent = String(rows.children.length).padStart(2,'0');
  addEvent('Proceso creado', `${name} · PID ${pid}`, 'green-dot');
});
document.getElementById('refresh').addEventListener('click', () => {
  addEvent('Panel actualizado', 'Se refrescó la vista de demostración', 'blue-dot');
});
document.getElementById('clearAlerts').addEventListener('click', () => {
  document.getElementById('alertCount').textContent = '00';
  document.querySelector('.counter').textContent = 'Revisadas';
  document.querySelector('.counter').style.color = '#16865b';
  document.querySelector('.counter').style.background = '#e7f7ef';
  addEvent('Alertas revisadas', 'El usuario marcó las alertas como revisadas', 'green-dot');
});
document.getElementById('addEvent').addEventListener('click', () => {
  addEvent('Evento de prueba', 'Registro manual desde la maqueta web', 'blue-dot');
});
document.querySelectorAll('.scenario').forEach(button => {
  button.addEventListener('click', () => {
    document.querySelectorAll('.scenario').forEach(b => b.classList.remove('selected'));
    button.classList.add('selected');
  });
});
document.getElementById('runScenario').addEventListener('click', () => {
  const selected = document.querySelector('.scenario.selected');
  const kind = selected?.dataset.scenario || 'normal';
  const messages = {
    normal: ['Escenario normal ejecutado', 'Actividad estable de procesos ficticios', 'green-dot'],
    suspicious: ['Consumo sospechoso simulado', 'Se generó una alerta de consumo elevado de CPU', 'red-dot'],
    attack: ['Amenaza de demostración ejecutada', 'Patrón anómalo ficticio detectado; no se ejecuta malware', 'red-dot']
  };
  const [title, detail, color] = messages[kind];
  addEvent(title, detail, color);
  if (kind !== 'normal') {
    document.getElementById('alertCount').textContent = '03';
    document.querySelector('.counter').textContent = '3 activas';
  }
});
