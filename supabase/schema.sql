-- CyberShield: esquema de persistencia para simulaciones didácticas
create extension if not exists pgcrypto;
create table if not exists public.cybershield_scenarios (
 id uuid primary key default gen_random_uuid(),
 name text not null,
 scenario_type text not null check (scenario_type in ('normal','sospechoso','personalizado')),
 started_at timestamptz not null default now(),
 finished_at timestamptz,
 metadata jsonb not null default '{}'::jsonb,
 created_at timestamptz not null default now()
);
create table if not exists public.cybershield_processes (
 id uuid primary key default gen_random_uuid(),
 scenario_id uuid references public.cybershield_scenarios(id) on delete set null,
 pid integer not null,
 name text not null,
 state text not null check (state in ('Listo','Ejecución','Bloqueado','Terminado')),
 priority smallint not null check (priority between 1 and 5),
 cpu_percent numeric(5,2) not null default 0 check (cpu_percent between 0 and 100),
 memory_mb numeric(12,2) not null default 0 check (memory_mb >= 0),
 simulated_at timestamptz not null default now(),
 created_at timestamptz not null default now(),
 updated_at timestamptz not null default now()
);
create index if not exists idx_cs_process_scenario on public.cybershield_processes(scenario_id);
create index if not exists idx_cs_process_pid on public.cybershield_processes(pid);
create index if not exists idx_cs_process_state on public.cybershield_processes(state);
create table if not exists public.cybershield_events (
 id uuid primary key default gen_random_uuid(),
 scenario_id uuid references public.cybershield_scenarios(id) on delete set null,
 process_id uuid references public.cybershield_processes(id) on delete set null,
 process_pid integer,
 event_type text not null,
 details text not null,
 occurred_at timestamptz not null default now(),
 metadata jsonb not null default '{}'::jsonb
);
create index if not exists idx_cs_events_occurred_at on public.cybershield_events(occurred_at desc);
create index if not exists idx_cs_events_type on public.cybershield_events(event_type);
create table if not exists public.cybershield_alerts (
 id uuid primary key default gen_random_uuid(),
 scenario_id uuid references public.cybershield_scenarios(id) on delete set null,
 process_id uuid references public.cybershield_processes(id) on delete set null,
 process_pid integer,
 alert_type text not null,
 severity text not null default 'media' check (severity in ('baja','media','alta','critica')),
 description text not null,
 detected_at timestamptz not null default now(),
 metadata jsonb not null default '{}'::jsonb
);
create index if not exists idx_cs_alerts_detected_at on public.cybershield_alerts(detected_at desc);
create index if not exists idx_cs_alerts_severity on public.cybershield_alerts(severity);
alter table public.cybershield_scenarios enable row level security;
alter table public.cybershield_processes enable row level security;
alter table public.cybershield_events enable row level security;
alter table public.cybershield_alerts enable row level security;
revoke all on public.cybershield_scenarios from anon, authenticated;
revoke all on public.cybershield_processes from anon, authenticated;
revoke all on public.cybershield_events from anon, authenticated;
revoke all on public.cybershield_alerts from anon, authenticated;
grant select, insert, update on public.cybershield_scenarios to authenticated;
grant select, insert, update on public.cybershield_processes to authenticated;
grant select, insert on public.cybershield_events to authenticated;
grant select, insert on public.cybershield_alerts to authenticated;
drop policy if exists "Authenticated users can manage CyberShield scenarios" on public.cybershield_scenarios;
create policy "Authenticated users can manage CyberShield scenarios" on public.cybershield_scenarios
 for all to authenticated using ((select auth.uid()) is not null) with check ((select auth.uid()) is not null);
drop policy if exists "Authenticated users can manage CyberShield processes" on public.cybershield_processes;
create policy "Authenticated users can manage CyberShield processes" on public.cybershield_processes
 for all to authenticated using ((select auth.uid()) is not null) with check ((select auth.uid()) is not null);
drop policy if exists "Authenticated users can read CyberShield events" on public.cybershield_events;
create policy "Authenticated users can read CyberShield events" on public.cybershield_events
 for select to authenticated using ((select auth.uid()) is not null);
drop policy if exists "Authenticated users can insert CyberShield events" on public.cybershield_events;
create policy "Authenticated users can insert CyberShield events" on public.cybershield_events
 for insert to authenticated with check ((select auth.uid()) is not null);
drop policy if exists "Authenticated users can read CyberShield alerts" on public.cybershield_alerts;
create policy "Authenticated users can read CyberShield alerts" on public.cybershield_alerts
 for select to authenticated using ((select auth.uid()) is not null);
drop policy if exists "Authenticated users can insert CyberShield alerts" on public.cybershield_alerts;
create policy "Authenticated users can insert CyberShield alerts" on public.cybershield_alerts
 for insert to authenticated with check ((select auth.uid()) is not null);
