import csv
import json
import os
import unicodedata

# -----------------------------------
# Internationalization / Traducciones
# -----------------------------------
TRANSLATIONS = {
    "es": {
        "app_title": "Cerrador Pro Enterprise",
        "login_title": "🔐 Login",
        "usuario": "Usuario",
        "password": "Contraseña",
        "ingresar": "Ingresar",
        "cerrar_sesion": "Cerrar sesión",
        "login_error": "Usuario o contraseña incorrecta, o cuenta inactiva.",
        "login_required": "Inicia sesión para acceder al panel",
        "panel": "Panel",
        "dashboard": "📊 Dashboard",
        "users": "👥 Usuarios",
        "clients": "📞 Clientes",
        "sales": "🛒 Ventas",
        "hotels_cruises": "🏨 Hoteles & Cruceros",
        "packages": "📦 Paquetes",
        "commissions": "💰 Comisiones",
        "statistics": "📈 Estadísticas",
        "sales_history": "📜 Historial de ventas",
        "settings": "⚙️ Configuración",
        "permissions": "🔐 Permisos",
        "home": "🏠 Inicio",
        "new_client": "📞 Nuevo Cliente",
        "registered_clients": "📋 Clientes Registrados",
        "destinations_cruises": "🌴 Destinos & Cruceros",
        "package_qualification": "📦 Calificación de Paquete",
        "calificaciones": "📑 Calificaciones",
        "my_commissions": "💰 Mis Comisiones",
        "my_statistics": "📈 Mis Estadísticas",
        "followups": "🗓️ Seguimientos",
        "my_profile": "⚙️ Mi Perfil",
        "language_label": "Idioma",
        "main_admin_screen": "Pantalla principal de administrador",
        "cards": "Tarjetas",
        "revenue": "Ingresos",
        "clients_card": "Clientes",
        "conversion": "Conversión",
        "unique_destinations": "Destinos únicos",
        "cruise_departures": "Salidas de crucero",
        "sales_per_day": "Ventas por día",
        "sales_per_advisor": "Ventas por asesor",
        "most_sold_packages": "Paquetes más vendidos",
        "monthly_growth": "Crecimiento mensual",
        "no_sales_data": "No hay datos de ventas aún.",
        "no_package_data": "No hay datos de paquetes aún.",
        "no_monthly_data": "No hay datos mensuales aún.",
        "cards_section": "Tarjetas",
        "create_user": "Crear asesor o admin",
        "save_user": "Guardar usuario",
        "block_unblock_user": "Bloquear / Desbloquear usuario",
        "delete_user": "Eliminar usuario",
        "update_user": "Actualizar usuario",
        "full_name": "Nombre completo",
        "state": "Estado",
        "age": "Edad",
        "marital_status": "Estado civil",
        "residency": "Residencia",
        "children_count": "Cantidad hijos",
        "children_ages": "Edades hijos (separadas por coma)",
        "assigned_advisor": "Asesor asignado",
        "follow_up_status": "Estado de seguimiento",
        "notes": "Notas",
        "save_client": "Guardar cliente",
        "search_client": "Buscar cliente",
        "work_schedules": "Horarios de trabajo",
        "zones": "Zonas",
        "commission_percentage": "Porcentaje de comisión",
        "save_config": "Guardar configuración",
        "config_saved": "Configuración guardada.",
        "zones_invalid": "El mapeo de zonas debe ser JSON válido",
        "total_sales": "Total de ventas",
        "sales_today": "Ventas hoy",
        "monthly_revenue_metric": "Ingresos mensuales",
        "active_advisors": "Asesores activos",
        "registered_clients_metric": "Clientes registrados",
        "pending_followups": "Seguimientos pendientes",
        "best_advisor": "Mejor asesor",
        "best_package": "Mejor paquete vendido",
        "best_destination": "Destino más vendido",
        "conversion_rate": "Tasa de conversión:",
        "total_commissions": "Comisiones totales:",
        "select_user": "Seleccionar usuario",
        "user_password": "Password",
        "user_role": "Rol",
        "user_status": "Estado",
        "user_name": "Nombre",
        "create_new_user": "Crear nuevo usuario",
        "full_name_label": "Nombre completo",
        "password_label": "Contraseña",
        "role_label": "Rol",
        "status_label": "Estado",
        "user_saved": "Usuario guardado.",
        "user_exists": "El usuario ya existe.",
        "user_deleted": "Usuario eliminado.",
        "password_required": "Usuario y contraseña son obligatorios.",
        "cannot_delete_own": "No puedes eliminar tu propia cuenta.",
        "user_updated": "Usuario actualizado.",
        "manage_users": "Gestionar usuarios existentes",
        "new_password": "Nueva contraseña",
        "update_user_btn": "Actualizar usuario",
        "block_user": "Bloquear / Desbloquear usuario",
        "delete_user_btn": "Eliminar usuario",
        "new_sale": "🛒 Nueva Venta",
        "client_name": "Cliente",
        "state_label": "Estado",
        "age_label": "Edad",
        "marital_status_label": "Estado civil",
        "residency_label": "Residencia",
        "children_count_label": "Cantidad de hijos",
        "children_ages_label": "Edades de hijos",
        "deductible": "Deducible",
        "commission_pct": "Porcentaje de comisión",
        "estimated_commission": "Comisión estimada",
        "clear_form": "Limpiar formulario",
        "register_sale": "Registrar Venta",
        "sale_registered": "Venta registrada correctamente",
        "benefits": "Beneficios",
        "recommended_destinations": "Destinos recomendados",
        "available_cruises": "Cruceros disponibles",
        "zone": "Zona",
        "hours": "Horario",
        "text_for_advisor": "Texto para asesor",
        "search": "Buscar",
        "filter_by": "Filtrar por",
        "select_client_delete": "Seleccionar cliente para borrar",
        "delete_client_btn": "Borrar cliente seleccionado",
        "client_deleted": "Cliente borrado.",
        "add_hotel": "Agregar hotel",
        "remove_hotel": "Eliminar hotel",
        "city": "Ciudad",
        "hotel_name": "Hotel",
        "add_hotel_btn": "Agregar hotel",
        "hotel_added": "Hotel agregado.",
        "hotel_exists": "El hotel ya existe.",
        "required_fields": "Ciudad y hotel son obligatorios.",
        "hotel_removed": "Hotel eliminado.",
        "add_cruise": "Agregar crucero",
        "category": "Categoría",
        "departure": "Salida",
        "route": "Ruta",
        "add_cruise_btn": "Agregar crucero",
        "cruise_added": "Crucero agregado.",
        "required_departure_route": "Departure y route son obligatorios.",
        "filter_by_advisor": "Filtrar por asesor",
        "filter_by_package": "Filtrar por paquete",
        "filter_by_status": "Filtrar por estado",
        "all": "Todos",
        "add_or_update": "Agregar o actualizar cliente",
        "interest_level": "Nivel de interés",
        "preferred_package": "Paquete preferido",
        "client_registered": "Cliente registrado.",
        "qualifies": "Califica para",
        "does_not_qualify": "No califica para VDL / HÍBRIDO. Enviar a MIX & MATCH.",
        "high": "Alto",
        "medium": "Medio",
        "low": "Bajo",
        "update_status": "Actualizar estado o agregar notas",
        "add_note": "Agregar nota",
        "save_changes": "Guardar cambios",
        "client_updated": "Cliente actualizado.",
        "no_pending": "No hay seguimientos pendientes.",
        "select_client_followup": "Seleccionar cliente",
        "new_status": "Nuevo estado",
        "add_note_label": "Agregar nota",
        "save_followup": "Guardar seguimiento",
        "followup_updated": "Seguimiento actualizado.",
        "export_csv": "Exportar CSV",
        "no_sales_registered": "No hay ventas registradas aún.",
        "select_sale_delete": "Seleccionar venta para borrar",
        "delete_sale_btn": "Borrar venta seleccionada",
        "sale_deleted": "Venta borrada.",
        "requirements": "Requisitos",
        "includes": "Incluye",
        "validity": "Vigencia",
        "destinations": "Destinos",
        "edit_package": "Editar paquete",
        "save_package": "Guardar",
        "package_updated": "Package",
        "updated": "actualizado.",
        "no_clients_registered": "No tienes clientes registrados aún.",
        "daily_commission": "Comisión del día",
        "weekly_commission": "Comisión semanal",
        "monthly_commission": "Comisión mensual",
        "total_earnings": "Ganancias totales",
        "sales_count": "Cantidad de ventas",
        "commission_percentage": "Porcentaje de comisión",
        "closed_sales": "Ventas cerradas",
        "lost_clients": "Clientes perdidos",
        "best_destination_label": "Mejor destino",
        "new_password_label": "Nueva contraseña",
        "update_password": "Actualizar contraseña",
        "password_updated": "Contraseña actualizada.",
        "enter_new_password": "Ingresa una nueva contraseña.",
    },
    "en": {
        "app_title": "Cerrador Pro Enterprise",
        "login_title": "🔐 Login",
        "usuario": "User",
        "password": "Password",
        "ingresar": "Sign in",
        "cerrar_sesion": "Sign out",
        "login_error": "Incorrect user or password, or inactive account.",
        "login_required": "Please sign in to access the dashboard",
        "panel": "Panel",
        "dashboard": "📊 Dashboard",
        "users": "👥 Users",
        "clients": "📞 Clients",
        "sales": "🛒 Sales",
        "hotels_cruises": "🏨 Hotels & Cruises",
        "packages": "📦 Packages",
        "commissions": "💰 Commissions",
        "statistics": "📈 Statistics",
        "sales_history": "📜 Sales History",
        "settings": "⚙️ Settings",
        "permissions": "🔐 Permissions",
        "home": "🏠 Home",
        "new_client": "📞 New Client",
        "registered_clients": "📋 Registered Clients",
        "destinations_cruises": "🌴 Destinations & Cruises",
        "package_qualification": "📦 Package Qualification",
        "calificaciones": "📑 Qualifications",
        "my_commissions": "💰 My Commissions",
        "my_statistics": "📈 My Statistics",
        "followups": "🗓️ Follow-ups",
        "my_profile": "⚙️ My Profile",
        "language_label": "Language",
        "main_admin_screen": "Main admin screen",
        "cards": "Cards",
        "revenue": "Revenue",
        "clients_card": "Clients",
        "conversion": "Conversion",
        "unique_destinations": "Unique destinations",
        "cruise_departures": "Cruise departures",
        "sales_per_day": "Sales per day",
        "sales_per_advisor": "Sales per advisor",
        "most_sold_packages": "Most sold packages",
        "monthly_growth": "Monthly growth",
        "no_sales_data": "No sales data yet.",
        "no_package_data": "No package data yet.",
        "no_monthly_data": "No monthly sales data.",
        "cards_section": "Cards",
        "create_user": "Create advisor or admin",
        "save_user": "Save user",
        "block_unblock_user": "Block / Unblock user",
        "delete_user": "Delete user",
        "update_user": "Update user",
        "full_name": "Full name",
        "state": "State",
        "age": "Age",
        "marital_status": "Marital status",
        "residency": "Residency",
        "children_count": "Children count",
        "children_ages": "Children ages (comma separated)",
        "assigned_advisor": "Assigned advisor",
        "follow_up_status": "Follow-up status",
        "notes": "Notes",
        "save_client": "Save client",
        "search_client": "Search client",
        "work_schedules": "Work schedules",
        "zones": "Zones",
        "commission_percentage": "Commission percentage",
        "save_config": "Save configuration",
        "config_saved": "Configuration saved.",
        "zones_invalid": "Zone mapping must be valid JSON",
    },
}


def tr(key):
    lang = st.session_state.get("lang", "es")
    return TRANSLATIONS.get(lang, TRANSLATIONS["es"]).get(key, key)
from datetime import datetime

import streamlit as st
import pandas as pd

# -----------------------------------
# ARCHIVOS Y DATOS
# -----------------------------------

USERS_FILE = "admin_usuarios.csv"
CLIENTS_FILE = "admin_clientes.csv"
SALES_FILE = "admin_ventas.csv"
HOTELS_FILE = "admin_hoteles_cruceros.json"
PACKAGES_FILE = "admin_packages.json"
CONFIG_FILE = "admin_config.json"

DEFAULT_USERS = {
    "mariajose": {
        "password": "admin2026",
        "rol": "admin",
        "name": "María Jose",
        "status": "active",
    },
    "juanpablo": {
        "password": "asesor2026",
        "rol": "advisor",
        "name": "Juan Pablo",
        "status": "active",
    },
}

DEFAULT_HOTELS_AND_CRUISES = {
    "hoteles": {
        "Orlando": ["Avanti", "Buena Vista Suites"],
        "Las Vegas": ["Tuscany Suites"],
        "Cancún": ["Oasis Palm Lite", "Villa del Palmar"],
        "Punta Cana": ["Ancora"],
        "Puerto Vallarta": ["Crown Paradise", "Krystal Vallarta"],
        "Los Cabos": ["Riu Santa Fe", "Marina Fiesta"],
        "Costa Rica": ["Fiesta Resort", "Occidental Papagayo"],
    },
    "cruises": {
        "5/4": [
            {"departure": "Miami (FL)", "route": "Key West + Cozumel"},
            {"departure": "Fort Lauderdale (FL)", "route": "Key West + Cozumel"},
            {"departure": "Port Canaveral (FL)", "route": "Bahamas + Nassau"},
            {"departure": "Jacksonville (FL)", "route": "Bahamas + Nassau"},
            {"departure": "Tampa (FL)", "route": "Cozumel"},
            {"departure": "Galveston (TX)", "route": "Cozumel"},
            {"departure": "New Orleans (LA)", "route": "Cozumel"},
            {"departure": "Long Beach (CA)", "route": "Catalina + Ensenada"},
        ],
        "6/5": [
            {"departure": "Charleston (SC)", "route": "Bahamas + Nassau"},
            {"departure": "Jacksonville (FL)", "route": "Bahamas + Nassau"},
            {"departure": "Miami (FL)", "route": "Jamaica + Grand Cayman"},
            {"departure": "Miami (FL)", "route": "Grand Turk + Amber Cove"},
            {"departure": "Tampa (FL)", "route": "Grand Cayman + Cozumel"},
            {"departure": "New Orleans (LA)", "route": "Progreso + Cozumel"},
        ],
    },
}

DEFAULT_PACKAGES = {
    "VDL": {
        "requirements": [
            "Married or living together",
            "US/Canada resident or citizen",
            "Women 25+",
            "Men 30+",
            "Families allowed",
            "Children under 11",
        ],
        "includes": [
            "All inclusive",
            "Airport transportation",
            "3 meals included",
            "Alcoholic drinks",
            "Non alcoholic drinks",
            "Premium stays",
            "3 destinations",
            "90 min Time Share",
        ],
        "validity": ["12 months to reserve", "18 months to travel"],
        "destinations": [
            "Cancun",
            "Punta Cana",
            "Puerto Vallarta",
            "Los Cabos",
            "Costa Rica",
            "Bahamas",
        ],
    },
    "HYBRID": {
        "requirements": [
            "Women 25+",
            "US/Canada resident or citizen",
            "No family requirement",
        ],
        "includes": [
            "1 VDL destination",
            "2 Mix & Match destinations",
            "90 min presentation",
        ],
        "validity": ["12 months reserve", "18 months travel"],
        "destinations": ["Cancun", "Las Vegas", "Orlando"],
    },
    "MIX & MATCH": {
        "requirements": [
            "18+",
            "Can travel with 21+ adult",
            "No residency required",
            "No Time Share",
        ],
        "includes": [
            "Open 4/3",
            "Cruise 5/4",
            "Cabin",
            "Snacks",
            "Attractions",
            "2 destinations",
        ],
        "validity": [
            "12 months first reservation",
            "12 additional months second reservation",
        ],
        "destinations": ["USA", "Canada", "Bahamas", "Mexico"],
    },
}


DEFAULT_CONFIG = {
    "zones": {
        "California": "Costa Oeste",
        "Texas": "Zona Central",
        "Florida": "Costa Este",
        "New York": "Costa Este",
        "Puerto Rico": "Puerto Rico",
    },
    "horarios": {
        "Costa Oeste": "6 AM - 2 PM",
        "Zona Central": "7 AM - 4 PM",
        "Costa Este": "9 AM - 5 PM",
        "Puerto Rico": "10 AM - 5 PM",
    },
    "porcentaje_default": 0.06,
    "follow_up_status": [
        "Interested",
        "Pending call",
        "Follow-up",
        "Closed sale",
        "No answer",
        "Not qualified",
    ],
    "permission_matrix": {
        "register_sales": {"advisor": True, "admin": True},
        "delete_users": {"advisor": False, "admin": True},
        "edit_packages": {"advisor": False, "admin": True},
        "view_stats": {"advisor": "Limited", "admin": "Full"},
    },
}

PERMISSION_DESCRIPTIONS = {
    "register_sales": "Register sales",
    "delete_users": "Delete users",
    "edit_packages": "Edit packages",
    "view_stats": "View stats",
}

# -----------------------------------
# UTILIDADES
# -----------------------------------

def ensure_file_exists(path, headers=None, default_data=None):
    if not os.path.exists(path):
        if headers:
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(headers)
        elif default_data is not None:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(default_data, f, ensure_ascii=False, indent=2)


def load_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


def save_csv(path, fieldnames, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def load_json(path, default_data):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(default_data, f, ensure_ascii=False, indent=2)
        return default_data
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default_data


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def parse_children_ages(raw_value):
    if isinstance(raw_value, str):
        parts = [part.strip() for part in raw_value.split(",") if part.strip()]
        return [int(part) for part in parts if part.isdigit()]
    if isinstance(raw_value, list):
        return [int(x) for x in raw_value if isinstance(x, int)]
    return []


def today_str():
    return datetime.now().strftime("%Y-%m-%d")


def format_money(value):
    return f"${value:,.2f}"


def calculate_qualification(client):
    residency = client.get("Residency")
    marital_status = client.get("Marital status")
    try:
        age = int(client.get("Age") or 0)
    except Exception:
        age = 0
    children_ages = parse_children_ages(client.get("Children ages", ""))

    if residency == "Sí":
        if marital_status == "Casado / Convive" and 25 <= age <= 79 and all(a <= 11 for a in children_ages):
            return "VDL"
        if marital_status == "Mujer Soltera" and 25 <= age <= 72:
            return "HÍBRIDO"
        if marital_status == "Hombre Soltero" and 35 <= age <= 59:
            return "VDL"
    if age >= 18 and all(a <= 17 for a in children_ages):
        return "MIX & MATCH"
    return "No qualify"


def calculate_commission(amount, percentage):
    try:
        return float(amount) * float(percentage)
    except Exception:
        return 0.0


def read_data():
    ensure_file_exists(USERS_FILE, headers=["Usuario", "Password", "Rol", "Status", "Name"])
    ensure_file_exists(CLIENTS_FILE, headers=[
        "ID",
        "Full name",
        "State",
        "Age",
        "Marital status",
        "Residency",
        "Children count",
        "Children ages",
        "Assigned advisor",
        "Qualification result",
        "Package",
        "Destination",
        "Follow-up status",
        "Notes",
        "Registration date",
    ])
    ensure_file_exists(SALES_FILE, headers=[
        "Date",
        "Client",
        "Advisor",
        "Package",
        "Destination",
        "Cruise",
        "Hotel",
        "Commission",
        "Follow-up status",
    ])
    ensure_file_exists(HOTELS_FILE, default_data=DEFAULT_HOTELS_AND_CRUISES)
    ensure_file_exists(PACKAGES_FILE, default_data=DEFAULT_PACKAGES)
    ensure_file_exists(CONFIG_FILE, default_data=DEFAULT_CONFIG)

    users = load_csv(USERS_FILE)
    if not users:
        users = []
        for username, info in DEFAULT_USERS.items():
            users.append({
                "Usuario": username,
                "Password": info["password"],
                "Rol": info["rol"],
                "Status": info["status"],
                "Name": info["name"],
            })
        save_csv(USERS_FILE, ["Usuario", "Password", "Rol", "Status", "Name"], users)
    clients = load_csv(CLIENTS_FILE)
    sales = load_csv(SALES_FILE)
    hotels_and_cruises = load_json(HOTELS_FILE, DEFAULT_HOTELS_AND_CRUISES)
    packages = load_json(PACKAGES_FILE, DEFAULT_PACKAGES)
    config = load_json(CONFIG_FILE, DEFAULT_CONFIG)
    return users, clients, sales, hotels_and_cruises, packages, config


def save_users(users):
    save_csv(USERS_FILE, ["Usuario", "Password", "Rol", "Status", "Name"], users)


def save_clients(clients):
    save_csv(CLIENTS_FILE, [
        "ID",
        "Full name",
        "State",
        "Age",
        "Marital status",
        "Residency",
        "Children count",
        "Children ages",
        "Assigned advisor",
        "Qualification result",
        "Package",
        "Destination",
        "Follow-up status",
        "Notes",
        "Registration date",
    ], clients)


def save_sales(sales):
    save_csv(SALES_FILE, [
        "Date",
        "Client",
        "Advisor",
        "Package",
        "Estado",
        "Age",
        "Marital status",
        "Residency",
        "Children count",
        "Children ages",
        "Destination",
        "Cruise",
        "Hotel",
        "Commission",
        "Follow-up status",
    ], sales)


def get_user(username, users):
    def normalize(s):
        if not s:
            return ""
        s = str(s).strip().lower()
        s = unicodedata.normalize("NFKD", s).encode("ASCII", "ignore").decode()
        return s.replace(" ", "")

    key = normalize(username)
    for u in users:
        if normalize(u.get("Usuario")) == key:
            return u
        if normalize(u.get("Name")) == key:
            return u
    return None


def build_summary(clients, sales, users, current_user=None):
    sales_total = len(sales)
    today = datetime.now().strftime("%Y-%m-%d")
    sales_today = sum(1 for s in sales if s["Date"].startswith(today))
    total_commissions = sum(float(s.get("Commission", 0) or 0) for s in sales)
    registered_clients = len(clients)
    active_advisors = sum(1 for u in users if u["Rol"] == "advisor" and u["Status"] == "active")
    pending_followups = sum(1 for c in clients if c["Follow-up status"] in ["Pending call", "Follow-up"])
    advisor_counts = {}
    package_counts = {}
    destination_counts = {}
    for s in sales:
        advisor_counts[s["Advisor"]] = advisor_counts.get(s["Advisor"], 0) + 1
        package_counts[s["Package"]] = package_counts.get(s["Package"], 0) + 1
        destination_counts[s["Destination"]] = destination_counts.get(s["Destination"], 0) + 1
    best_advisor = max(advisor_counts, key=advisor_counts.get) if advisor_counts else "N/A"
    best_package = max(package_counts, key=package_counts.get) if package_counts else "N/A"
    best_destination = max(destination_counts, key=destination_counts.get) if destination_counts else "N/A"
    conversion_rate = f"{(sales_total / registered_clients * 100):.1f}%" if registered_clients else "0%"
    monthly_revenue = total_commissions  # simplistic as commission total
    if current_user:
        advisor_sales = [s for s in sales if s["Advisor"] == current_user]
        advisor_commission = sum(float(s.get("Commission", 0) or 0) for s in advisor_sales)
    else:
        advisor_commission = 0
    return {
        "sales_total": sales_total,
        "sales_today": sales_today,
        "monthly_revenue": monthly_revenue,
        "active_advisors": active_advisors,
        "registered_clients": registered_clients,
        "pending_followups": pending_followups,
        "best_advisor": best_advisor,
        "best_package": best_package,
        "best_destination": best_destination,
        "conversion_rate": conversion_rate,
        "total_commissions": total_commissions,
        "advisor_commission": advisor_commission,
    }

# -----------------------------------
# APP UI
# -----------------------------------

st.set_page_config(page_title="Cerrador Pro Enterprise", page_icon="💼", layout="wide")

st.markdown(
    """
    <style>
    /* Light theme */
    .stApp {
        background-color: #f4f6f8;
        color: #0f1724;
    }
    .card {
        padding: 20px;
        border-radius: 14px;
        background: white;
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
        margin-bottom: 16px;
        color: #0f1724;
    }
    .card h3 { margin: 0 0 8px 0; }
    .card-value { font-size: 28px; font-weight: 700; margin-bottom: 6px; }
    .metric { color: #6b7280; }
    .success-box { border-left: 6px solid #2ecc71; background: #eefaf1; color: #145a32; padding: 14px; border-radius: 12px; }
    .warning-box { border-left: 6px solid #e74c3c; background: #fdecec; color: #78281f; padding: 14px; border-radius: 12px; }

    /* Dark theme */
    @media (prefers-color-scheme: dark) {
        .stApp { background-color: #0b1220; color: #e6eef8; }
        .card { background: #0f1724; box-shadow: none; color: #e6eef8; }
        .metric { color: #9aa6b2; }
        .success-box { border-left-color: #2ecc71; background: rgba(46,204,113,0.08); color: #b7f5d0; }
        .warning-box { border-left-color: #e74c3c; background: rgba(231,76,60,0.06); color: #f5c2bd; }
        .stButton>button { color: #e6eef8; }
        .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>select {
            background: #071127; color: #e6eef8; border: 1px solid #213042;
        }
    }

    /* Also support Streamlit theme attribute */
    [data-theme="dark"] .stApp { background-color: #0b1220; color: #e6eef8; }
    [data-theme="dark"] .card { background: #0f1724; color: #e6eef8; }
    [data-theme="dark"] .metric { color: #9aa6b2; }
    </style>
    """,
    unsafe_allow_html=True,
)

ensure_file_exists(USERS_FILE, headers=["Usuario", "Password", "Rol", "Status", "Name"])
ensure_file_exists(CLIENTS_FILE, headers=[
    "ID",
    "Full name",
    "State",
    "Age",
    "Marital status",
    "Residency",
    "Children count",
    "Children ages",
    "Assigned advisor",
    "Qualification result",
    "Package",
    "Destination",
    "Follow-up status",
    "Notes",
    "Registration date",
])
ensure_file_exists(SALES_FILE, headers=[
    "Date",
    "Client",
    "Advisor",
    "Package",
    "Estado",
    "Age",
    "Marital status",
    "Residency",
    "Children count",
    "Children ages",
    "Destination",
    "Cruise",
    "Hotel",
    "Commission",
    "Follow-up status",
])
ensure_file_exists(HOTELS_FILE, default_data=DEFAULT_HOTELS_AND_CRUISES)
ensure_file_exists(PACKAGES_FILE, default_data=DEFAULT_PACKAGES)
ensure_file_exists(CONFIG_FILE, default_data=DEFAULT_CONFIG)

users, clients, sales, hotels_and_cruises, packages, config = read_data()

if "lang" not in st.session_state:
    st.session_state.lang = "es"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = ""
    st.session_state.rol = ""
    st.session_state.name = ""

st.sidebar.selectbox(tr("language_label"), ["Español", "English"], index=0 if st.session_state.lang == "es" else 1, key="lang_select")
if st.session_state.get("lang_select") == "Español":
    st.session_state.lang = "es"
else:
    st.session_state.lang = "en"

st.sidebar.title(tr("login_title"))
usuario = st.sidebar.text_input(tr("usuario"), key="login_usuario")
password = st.sidebar.text_input(tr("password"), type="password", key="login_password")

if st.sidebar.button(tr("ingresar")):
    usuario_key = usuario.strip().lower()
    user = get_user(usuario_key, users)
    if user and user["Password"] == password and user["Status"] == "active":
        st.session_state.logged_in = True
        st.session_state.user = usuario_key
        st.session_state.name = user.get("Name", usuario_key)
        st.session_state.rol = user.get("Rol", "advisor")
        st.sidebar.success(f"{ 'Bienvenido' if st.session_state.lang == 'es' else 'Welcome' } {st.session_state.name}")
    else:
        st.sidebar.error(tr("login_error"))

if st.session_state.logged_in:
    if st.sidebar.button(tr("cerrar_sesion")):
        st.session_state.logged_in = False
        st.session_state.user = ""
        st.session_state.name = ""
        st.session_state.rol = ""
        st.rerun()

if not st.session_state.logged_in:
    st.warning(tr("login_required"))
    st.stop()

role = st.session_state.rol
username = st.session_state.user
name = st.session_state.name

admin_menu_keys = [
    "dashboard",
    "users",
    "registered_clients",
    "new_client",
    "sales",
    "packages",
    "commissions",
    "destinations_cruises",
    "sales_history",
    "package_qualification",
    
    "followups",
    "my_profile",
]

advisor_menu_keys = [
    "home",
    "new_client",
    "sales",
    "registered_clients",
    "destinations_cruises",
    "package_qualification",
    
    "my_commissions",
    "my_statistics",
    "followups",
    "sales_history",
    "my_profile",
]

menu_keys = admin_menu_keys if role == "admin" else advisor_menu_keys

# radio returns the key; labels are shown via format_func using translations
page = st.sidebar.radio(tr("panel"), menu_keys, format_func=lambda k: tr(k))

summary = build_summary(clients, sales, users, current_user=name if role == "advisor" else None)


# -----------------------------------
# PÁGINAS ADMIN
# -----------------------------------

def dashboard_page():
    st.title(tr("dashboard"))
    st.markdown(f"### {tr('main_admin_screen')}")
    col1, col2, col3 = st.columns(3)
    col1.metric(tr("total_sales"), summary["sales_total"])
    col2.metric(tr("sales_today"), summary["sales_today"])
    col3.metric(tr("monthly_revenue_metric"), format_money(summary["monthly_revenue"]))
    col4, col5, col6 = st.columns(3)
    col4.metric(tr("active_advisors"), summary["active_advisors"])
    col5.metric(tr("registered_clients_metric"), summary["registered_clients"])
    col6.metric(tr("pending_followups"), summary["pending_followups"])
    col7, col8, col9 = st.columns(3)
    col7.metric(tr("best_advisor"), summary["best_advisor"])
    col8.metric(tr("best_package"), summary["best_package"])
    col9.metric(tr("best_destination"), summary["best_destination"])
    st.markdown(f"**{tr('conversion_rate')}** {summary['conversion_rate']}")
    st.markdown(f"**{tr('total_commissions')}** {format_money(summary['total_commissions'])}")
    st.markdown("---")
    st.markdown(f"### {tr('cards')}")
    card_col1, card_col2, card_col3 = st.columns(3)
    card_col1.markdown("""
        <div class='card'>
            <h3>💰 %s</h3>
            <div class='card-value'>%s</div>
            <div class='metric'>%s</div>
        </div>
    """ % (tr("revenue"), format_money(summary["monthly_revenue"]), tr("revenue")), unsafe_allow_html=True)
    card_col2.markdown("""
        <div class='card'>
            <h3>📞 %s</h3>
            <div class='card-value'>%s</div>
            <div class='metric'>%s</div>
        </div>
    """ % (tr("clients_card"), summary["registered_clients"], tr("clients_card")), unsafe_allow_html=True)
    card_col3.markdown("""
        <div class='card'>
            <h3>📈 %s</h3>
            <div class='card-value'>%s</div>
            <div class='metric'>%s</div>
        </div>
    """ % (tr("conversion"), summary["conversion_rate"], tr("conversion")), unsafe_allow_html=True)
    extra_col1, extra_col2, extra_col3 = st.columns(3)
    extra_col1.markdown("""
        <div class='card'>
            <h3>👨‍💼 %s</h3>
            <div class='card-value'>%s</div>
            <div class='metric'>%s</div>
        </div>
    """ % (tr("clients_card"), summary["active_advisors"], tr("clients_card")), unsafe_allow_html=True)
    extra_col2.markdown("""
        <div class='card'>
            <h3>🌴 %s</h3>
            <div class='card-value'>%s</div>
            <div class='metric'>%s</div>
        </div>
    """ % (tr("unique_destinations"), len(set([s["Destination"] for s in sales if s.get("Destination")])), tr("unique_destinations")) , unsafe_allow_html=True)
    extra_col3.markdown("""
        <div class='card'>
            <h3>🚢 %s</h3>
            <div class='card-value'>%s</div>
            <div class='metric'>%s</div>
        </div>
    """ % (tr("cruise_departures"), sum(len(v) for v in hotels_and_cruises["cruises"].values()), tr("cruise_departures")), unsafe_allow_html=True)
    st.markdown("---")
    st.subheader(tr("sales_per_day"))
    daily = {}
    for sale in sales:
        day = sale["Date"][:10]
        daily[day] = daily.get(day, 0) + 1
    if daily:
        st.bar_chart(daily)
    else:
        st.info(tr("no_sales_data"))
    st.subheader(tr("sales_per_advisor"))
    advisor_counts = {}
    for sale in sales:
        advisor_counts[sale["Advisor"]] = advisor_counts.get(sale["Advisor"], 0) + 1
    if advisor_counts:
        st.bar_chart(advisor_counts)
    else:
        st.info(tr("no_sales_data"))
    st.subheader(tr("most_sold_packages"))
    package_counts = {}
    for sale in sales:
        package_counts[sale["Package"]] = package_counts.get(sale["Package"], 0) + 1
    if package_counts:
        st.bar_chart(package_counts)
    else:
        st.info(tr("no_package_data"))
    st.subheader(tr("monthly_growth"))
    monthly = {}
    for sale in sales:
        month = sale["Date"][:7]
        monthly[month] = monthly.get(month, 0) + 1
    if monthly:
        st.line_chart(monthly)
    else:
        st.info(tr("no_monthly_data"))


def users_page():
    st.title(tr("users"))
    st.markdown(f"### {tr('users')}")
    st.dataframe(users)
    st.markdown("---")
    st.subheader(tr("create_user"))
    with st.form("create_user"):
        new_user = st.text_input(tr("usuario"))
        new_name = st.text_input(tr("full_name"))
        new_password = st.text_input(tr("password"), type="password")
        role = st.selectbox(tr("role_label"), ["admin", "advisor"])
        status = st.selectbox(tr("status_label"), ["active", "inactive"])
        if st.form_submit_button(tr("save_user")):
            if not new_user or not new_password:
                st.error(tr("password_required"))
            else:
                if get_user(new_user.strip().lower(), users):
                    st.error(tr("user_exists"))
                else:
                    users.append({
                        "Usuario": new_user.strip().lower(),
                        "Password": new_password,
                        "Rol": role,
                        "Status": status,
                        "Name": new_name.strip() or new_user.strip(),
                    })
                    save_users(users)
                    st.success(tr("user_saved"))
                    st.rerun()
    st.markdown("---")
    st.subheader(tr("manage_users"))
    selected = st.selectbox(tr("select_user"), [u["Usuario"] for u in users])
    if selected:
        user = get_user(selected, users)
        if user:
            st.write(f"**{tr('full_name')}:** {user['Name']}")
            st.write(f"**Rol:** {user['Rol']}")
            st.write(f"**{tr('status_label')}:** {user['Status']}")
            col1, col2 = st.columns(2)
            if col1.button(tr("block_unblock_user")):
                user["Status"] = "inactive" if user["Status"] == "active" else "active"
                save_users(users)
                st.success("Estado actualizado.")
                st.rerun()
            if col2.button(tr("delete_user_btn")):
                if user["Usuario"] == username:
                    st.error(tr("cannot_delete_own"))
                else:
                    users[:] = [u for u in users if u["Usuario"] != user["Usuario"]]
                    save_users(users)
                    st.success(tr("user_deleted"))
                    st.rerun()
            new_pass = st.text_input(tr("new_password_label"), type="password")
            new_role = st.selectbox(tr("role_label"), ["admin", "advisor"], index=0 if user["Rol"] == "admin" else 1)
            if st.button(tr("update_user_btn")):
                if new_pass:
                    user["Password"] = new_pass
                user["Rol"] = new_role
                save_users(users)
                st.success(tr("user_updated"))
                st.rerun()


def clients_page():
    st.title(tr("clients"))
    st.markdown(f"### {tr('clients')}")
    search_name = st.text_input(tr("search_client"))
    filter_advisor = st.selectbox(tr("filter_by_advisor"), [tr("all")] + [u["Name"] for u in users if u["Rol"] == "advisor"])
    filter_package = st.selectbox(tr("filter_by_package"), [tr("all"), "VDL", "HÍBRIDO", "MIX & MATCH"])
    filter_status = st.selectbox(tr("filter_by_status"), [tr("all")] + config["follow_up_status"])
    filtered = clients
    if search_name:
        filtered = [c for c in filtered if search_name.lower() in c["Full name"].lower()]
    if filter_advisor != tr("all"):
        filtered = [c for c in filtered if c["Assigned advisor"] == filter_advisor]
    if filter_package != tr("all"):
        filtered = [c for c in filtered if c["Package"] == filter_package]
    if filter_status != tr("all"):
        filtered = [c for c in filtered if c["Follow-up status"] == filter_status]

    st.dataframe(filtered)
    st.markdown("---")
    with st.form("client_form"):
        full_name = st.text_input(tr("full_name"))
        state = st.text_input(tr("state"))
        age = st.number_input(tr("age"), min_value=18, max_value=100, value=30)
        marital_status = st.selectbox(tr("marital_status"), ["Casado / Convive", "Mujer Soltera", "Hombre Soltero"])
        residency = st.selectbox(tr("residency"), ["Sí", "No"])
        children_count = st.number_input(tr("children_count"), min_value=0, max_value=10, value=0)
        children_ages = st.text_input(tr("children_ages"))
        assigned_advisor = st.selectbox(tr("assigned_advisor"), [u["Name"] for u in users if u["Rol"] == "advisor"])
        follow_up_status = st.selectbox(tr("follow_up_status"), config["follow_up_status"])
        notes = st.text_area(tr("notes"))
        if st.form_submit_button(tr("save_client")):
            qualification = calculate_qualification({
                "Residency": residency,
                "Marital status": marital_status,
                "Age": age,
                "Children ages": children_ages,
            })
            package = qualification if qualification != "No qualify" else "MIX & MATCH"
            destination = "Cancún" if package == "VDL" else "Las Vegas" if package == "HÍBRIDO" else "Bahamas"
            client_id = str(len(clients) + 1)
            clients.append({
                "ID": client_id,
                "Full name": full_name,
                "State": state,
                "Age": str(age),
                "Marital status": marital_status,
                "Residency": residency,
                "Children count": str(children_count),
                "Children ages": children_ages,
                "Assigned advisor": assigned_advisor,
                "Qualification result": qualification,
                "Package": package,
                "Destination": destination,
                "Follow-up status": follow_up_status,
                "Notes": notes,
                "Registration date": today_str(),
            })
            save_clients(clients)
            st.success("Cliente guardado.")
            st.rerun()

    st.markdown("---")
    st.subheader("Manage filtered client")
    selected_client = st.selectbox(tr("select_client_delete"), [c["ID"] + " - " + c["Full name"] for c in filtered] if filtered else [])
    if selected_client:
        selected_id = selected_client.split(" - ")[0]
        client = next((c for c in clients if c["ID"] == selected_id), None)
        if client:
            if st.button(tr("delete_client_btn")):
                clients[:] = [c for c in clients if c["ID"] != selected_id]
                save_clients(clients)
                st.success(tr("client_deleted"))
                st.rerun()


def sales_page():
    st.title(tr("sales"))
    st.markdown("### Registro de ventas")

    zonas = {
        "Alabama": "Costa Este",
        "Alaska": "Costa Oeste",
        "Arizona": "Costa Oeste",
        "Arkansas": "Zona Central",
        "California": "Costa Oeste",
        "North Carolina": "Costa Este",
        "South Carolina": "Costa Este",
        "Colorado": "Costa Oeste",
        "Connecticut": "Costa Este",
        "North Dakota": "Zona Central",
        "South Dakota": "Zona Central",
        "Delaware": "Costa Este",
        "Florida": "Costa Este",
        "Georgia": "Costa Este",
        "Hawaii": "Costa Oeste",
        "Idaho": "Costa Oeste",
        "Illinois": "Zona Central",
        "Indiana": "Zona Central",
        "Iowa": "Zona Central",
        "Kansas": "Zona Central",
        "Kentucky": "Zona Central",
        "Louisiana": "Zona Central",
        "Maine": "Costa Este",
        "Maryland": "Costa Este",
        "Massachusetts": "Costa Este",
        "Michigan": "Zona Central",
        "Minnesota": "Zona Central",
        "Mississippi": "Zona Central",
        "Missouri": "Zona Central",
        "Montana": "Costa Oeste",
        "Nebraska": "Zona Central",
        "Nevada": "Costa Oeste",
        "New Jersey": "Costa Este",
        "New York": "Costa Este",
        "New Hampshire": "Costa Este",
        "New Mexico": "Costa Oeste",
        "Ohio": "Zona Central",
        "Oklahoma": "Zona Central",
        "Oregon": "Costa Oeste",
        "Pennsylvania": "Costa Este",
        "Rhode Island": "Costa Este",
        "Tennessee": "Zona Central",
        "Texas": "Zona Central",
        "Utah": "Costa Oeste",
        "Vermont": "Costa Este",
        "Virginia": "Costa Este",
        "West Virginia": "Costa Este",
        "Washington": "Costa Oeste",
        "Wisconsin": "Zona Central",
        "Wyoming": "Costa Oeste",
    }

    horarios = {
        "Costa Oeste": "6 AM - 2 PM",
        "Zona Central": "7 AM - 4 PM",
        "Costa Este": "9 AM - 5 PM",
    }

    destinos_vdl = [
        "Cancún",
        "Punta Cana",
        "Puerto Vallarta",
        "Los Cabos",
        "Bahamas",
        "Costa Rica",
    ]

    destinos_mix = [
        "Las Vegas",
        "Phoenix",
        "San Diego",
        "Los Ángeles",
        "Bahamas",
        "México",
    ]

    cruceros = {
        "Miami": "Key West + Cozumel",
        "Port Canaveral": "Bahamas + Nassau",
        "Long Beach": "Ensenada + Islas Catalina",
        "New Orleans": "Cozumel + Progreso",
    }

    def hijos_validos_vdl(edades):
        return all(edad_hijo <= 11 for edad_hijo in edades)

    def hijos_validos_mix(edades):
        return all(edad_hijo <= 17 for edad_hijo in edades)

    if "sale_cliente" not in st.session_state:
        st.session_state.sale_cliente = ""
    if "sale_estado" not in st.session_state:
        st.session_state.sale_estado = sorted(zonas.keys())[0]
    if "sale_estado_civil" not in st.session_state:
        st.session_state.sale_estado_civil = "Casado / Convive"
    if "sale_edad" not in st.session_state:
        st.session_state.sale_edad = 30
    if "sale_residencia" not in st.session_state:
        st.session_state.sale_residencia = "Sí"
    if "sale_cantidad_hijos" not in st.session_state:
        st.session_state.sale_cantidad_hijos = 0

    cliente = st.text_input("Cliente", key="sale_cliente")
    estado = st.selectbox("Estado", sorted(zonas.keys()), key="sale_estado")
    estado_civil = st.selectbox(
        "Estado civil",
        [
            "Casado / Convive",
            "Mujer Soltera",
            "Hombre Soltero",
        ],
        key="sale_estado_civil",
    )
    edad = st.number_input("Edad", 18, 100, 30, key="sale_edad")
    residencia = st.selectbox("Residencia", ["Sí", "No"], key="sale_residencia")
    cantidad_hijos = st.number_input("Cantidad hijos", 0, 10, 0, key="sale_cantidad_hijos")
    edades_hijos = []
    if cantidad_hijos > 0:
        st.subheader("Edades hijos")
        for i in range(cantidad_hijos):
            clave_hijo = f"sale_hijo_{i}"
            if clave_hijo not in st.session_state:
                st.session_state[clave_hijo] = 0
            edad_hijo = st.number_input(f"Edad hijo {i+1}", 0, 25, value=st.session_state[clave_hijo], key=clave_hijo)
            edades_hijos.append(edad_hijo)

    paquete = "MIX & MATCH"
    vigencia = "24 meses"
    beneficios = []
    destinos = []
    califica = False

    if residencia == "Sí":
        if estado_civil == "Casado / Convive":
            if 30 <= edad <= 70:
                if hijos_validos_vdl(edades_hijos):
                    paquete = "VDL"
                    vigencia = "12 meses reservar / 18 vacacionar"
                    beneficios = [
                        "All inclusive",
                        "3 comidas",
                        "Bebidas alcohólicas",
                        "Transporte aeropuerto-hotel",
                        "90 mins Time Share",
                    ]
                    destinos = destinos_vdl
                    califica = True
        elif estado_civil == "Mujer Soltera":
            if 25 <= edad <= 70:
                paquete = "HÍBRIDO"
                beneficios = [
                    "1 destino VDL",
                    "2 Mix & Match",
                    "90 mins Time Share",
                ]
                destinos = ["Cancún", "Las Vegas", "Orlando"]
                califica = True
        elif estado_civil == "Hombre Soltero":
            if 35 <= edad <= 59:
                paquete = "VDL"
                beneficios = [
                    "All inclusive",
                    "Hospedaje premium",
                    "Transporte incluido",
                ]
                destinos = ["Puerto Vallarta", "Los Cabos", "Lake Havasu"]
                califica = True

    if not califica:
        if edad >= 18:
            if hijos_validos_mix(edades_hijos):
                paquete = "MIX & MATCH"
                beneficios = [
                    "Sin Time Share",
                    "Open 4/3",
                    "Crucero 5/4",
                    "12 meses para reservar",
                ]
                destinos = destinos_mix

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Resultado")
        if paquete == "VDL":
            st.success(f"✅ CALIFICA PARA VDL — Vigencia: {vigencia}")
        elif paquete == "HÍBRIDO":
            st.success("✅ CALIFICA PARA HÍBRIDO")
        else:
            st.warning("⚠️ ENVIAR A MIX & MATCH")

        st.subheader("Beneficios")
        for beneficio in beneficios:
            st.write("✅", beneficio)

        st.subheader("Destinos recomendados")
        for destino in destinos:
            st.write("🌴", destino)

        st.subheader("Cruceros disponibles")
        for salida, ruta in cruceros.items():
            st.write(f"🚢 {salida} → {ruta}")

    with col2:
        zona = zonas[estado]
        st.subheader("Zona")
        st.info(f"Zona: {zona}\n\nHorario: {horarios[zona]}")

        deducible = st.number_input("Deducible", 200, 500, 399)
        porcentaje = st.selectbox("Porcentaje comisión", [6, 8])
        comision = deducible * (porcentaje / 100)
        st.metric("Comisión estimada", f"${comision:,.2f}")

        def limpiar_formulario():
            st.session_state.sale_cliente = ""
            st.session_state.sale_estado = sorted(zonas.keys())[0]
            st.session_state.sale_estado_civil = "Casado / Convive"
            st.session_state.sale_edad = 30
            st.session_state.sale_residencia = "Sí"
            st.session_state.sale_cantidad_hijos = 0
            for i in range(10):
                clave_hijo = f"sale_hijo_{i}"
                if clave_hijo in st.session_state:
                    del st.session_state[clave_hijo]

        st.button("Limpiar formulario", on_click=limpiar_formulario)

        advisor_name = name or "Tu asesor"
        client_label = cliente or "cliente"
        speech_text = f"Hola {client_label},\n\nSoy {advisor_name} y quiero proponerte el paquete {paquete}. "
        if paquete == "VDL":
            speech_text += "Este paquete es ideal para tu perfil porque ofrece hospedaje premium, transporte incluido y acceso a experiencias All Inclusive."
        elif paquete == "HÍBRIDO":
            speech_text += "Lo recomiendo para tu perfil como mujer soltera, ya que combina un destino VDL con opciones flexibles Mix & Match."
        else:
            speech_text += "Con MIX & MATCH puedes reservar en varios destinos y aprovechar una vigencia flexible sin Time Share."
        speech_text += f"\n\nTu destino recomendado es {destinos[0] if destinos else 'un destino disponible'}.\n\n¿Te gustaría avanzar con esta opción?"

        st.subheader("Texto para asesor")
        st.text_area("Copy para cerrar la venta", speech_text, height=180)

        if st.button("Registrar Venta"):
            sales.append({
                "Date": datetime.now().isoformat(sep=" ", timespec="seconds"),
                "Client": cliente,
                "Advisor": name,
                "Package": paquete,
                "Estado": estado,
                "Age": str(edad),
                "Marital status": estado_civil,
                "Residency": residencia,
                "Children count": str(cantidad_hijos),
                "Children ages": ", ".join(str(x) for x in edades_hijos),
                "Destination": destinos[0] if destinos else "",
                "Cruise": ", ".join([f"{k} → {v}" for k, v in cruceros.items()]),
                "Hotel": "",
                "Commission": f"{comision:.2f}",
                "Follow-up status": "Closed sale",
            })
            save_sales(sales)
            st.success("Venta registrada correctamente")


def hotels_cruises_page():
    st.title(tr("hotels_cruises"))
    st.markdown("### Admin manages destinations dynamically")
    st.subheader("Hoteles")
    for city, hotel_list in hotels_and_cruises["hoteles"].items():
        st.markdown(f"**{city}**")
        for h in hotel_list:
            st.write(f"- {h}")
    st.markdown("---")
    st.subheader("Add hotel")
    with st.form("add_hotel"):
        city = st.text_input("City")
        hotel_name = st.text_input("Hotel")
        if st.form_submit_button("Agregar hotel"):
            if city and hotel_name:
                hotels_and_cruises["hoteles"].setdefault(city, [])
                if hotel_name not in hotels_and_cruises["hoteles"][city]:
                    hotels_and_cruises["hoteles"][city].append(hotel_name)
                    save_json(HOTELS_FILE, hotels_and_cruises)
                    st.success("Hotel agregado.")
                    st.rerun()
                else:
                    st.warning("El hotel ya existe.")
            else:
                st.error("Ciudad y hotel son obligatorios.")
    st.subheader("Remove hotel")
    with st.form("remove_hotel"):
        city_remove = st.selectbox("Ciudad", [c for c in hotels_and_cruises["hoteles"].keys()])
        hotel_remove = st.selectbox("Hotel", hotels_and_cruises["hoteles"].get(city_remove, []))
        if st.form_submit_button("Eliminar hotel"):
            hotels_and_cruises["hoteles"][city_remove].remove(hotel_remove)
            if not hotels_and_cruises["hoteles"][city_remove]:
                del hotels_and_cruises["hoteles"][city_remove]
            save_json(HOTELS_FILE, hotels_and_cruises)
            st.success("Hotel eliminado.")
            st.rerun()
    st.markdown("---")
    st.subheader("Cruises")
    for category, cruise_list in hotels_and_cruises["cruises"].items():
        st.markdown(f"**{category} Cruises**")
        for cruise in cruise_list:
            st.write(f"- {cruise['departure']} → {cruise['route']}")
    st.markdown("---")
    st.subheader("Add cruise")
    with st.form("add_cruise"):
        category = st.selectbox("Category", ["5/4", "6/5"])
        departure = st.text_input("Departure")
        route = st.text_input("Route")
        if st.form_submit_button("Agregar cruise"):
            if departure and route:
                hotels_and_cruises["cruises"].setdefault(category, [])
                hotels_and_cruises["cruises"][category].append({"departure": departure, "route": route})
                save_json(HOTELS_FILE, hotels_and_cruises)
                st.success("Cruise agregado.")
                st.rerun()
            else:
                st.error("Departure y route son obligatorios.")


def packages_page():
    st.title(tr("packages"))
    st.markdown("### Admin can fully edit package rules")
    for package_name, info in packages.items():
        st.subheader(package_name)
        requirements = st.text_area(f"Requirements {package_name}", value="\n".join(info["requirements"]), key=f"req_{package_name}")
        includes = st.text_area(f"Includes {package_name}", value="\n".join(info["includes"]), key=f"inc_{package_name}")
        validity = st.text_area(f"Validity {package_name}", value="\n".join(info["validity"]), key=f"val_{package_name}")
        destinations = st.text_area(f"Destinations {package_name}", value="\n".join(info["destinations"]), key=f"dest_{package_name}")
        if st.button(f"Guardar {package_name}", key=f"save_pkg_{package_name}"):
            packages[package_name]["requirements"] = [line.strip() for line in requirements.split("\n") if line.strip()]
            packages[package_name]["includes"] = [line.strip() for line in includes.split("\n") if line.strip()]
            packages[package_name]["validity"] = [line.strip() for line in validity.split("\n") if line.strip()]
            packages[package_name]["destinations"] = [line.strip() for line in destinations.split("\n") if line.strip()]
            save_json(PACKAGES_FILE, packages)
            st.success(f"Package {package_name} updated.")
            st.rerun()


def commissions_page():
    st.title(tr("commissions"))
    advisor_totals = {}
    advisor_sales = {}
    for sale in sales:
        advisor_totals[sale["Advisor"]] = advisor_totals.get(sale["Advisor"], 0) + float(sale.get("Commission", 0) or 0)
        advisor_sales[sale["Advisor"]] = advisor_sales.get(sale["Advisor"], 0) + 1
    total = summary["total_commissions"]
    st.metric("Comisión total", format_money(total))
    rows = []
    for advisor, amount in advisor_totals.items():
        rows.append({"Advisor": advisor, "Sales": advisor_sales.get(advisor, 0), "Earnings": format_money(amount)})
    st.dataframe(rows)
    st.subheader("Ventas individuales")
    st.dataframe(sales)


def statistics_page():
    st.title(tr("statistics"))
    st.metric("Best advisor", summary["best_advisor"])
    st.metric("Most sold package", summary["best_package"])
    st.metric("Most sold destination", summary["best_destination"])
    st.metric("Conversion percentage", summary["conversion_rate"])
    states = {}
    package_clients = {}
    monthly_clients = {}
    daily_performance = {}
    for client in clients:
        states[client["State"]] = states.get(client["State"], 0) + 1
        package_clients[client["Package"]] = package_clients.get(client["Package"], 0) + 1
        month = client["Registration date"][:7]
        monthly_clients[month] = monthly_clients.get(month, 0) + 1
    for sale in sales:
        day = sale["Date"][:10]
        daily_performance[day] = daily_performance.get(day, 0) + 1
    if states:
        st.subheader("Sales by state")
        st.bar_chart(states)
    if package_clients:
        st.subheader("Clients by package")
        st.pie_chart(pd.Series(package_clients))
    if monthly_clients:
        st.subheader("Monthly growth")
        st.line_chart(monthly_clients)
    if daily_performance:
        st.subheader("Daily performance")
        st.line_chart(daily_performance)


def sales_history_page(is_admin=True):
    st.title(tr("sales_history"))
    st.markdown("### Full database of all sales")
    if sales:
        search_client = st.text_input("Buscar cliente")
        filter_advisor = st.text_input("Filtrar por asesor") if not is_admin else st.selectbox("Filtrar por asesor", ["Todos"] + [u["Name"] for u in users if u["Rol"] == "advisor"])
        filtered = sales
        if search_client:
            filtered = [s for s in filtered if search_client.lower() in s["Client"].lower()]
        if filter_advisor and filter_advisor != "Todos":
            filtered = [s for s in filtered if s["Advisor"] == filter_advisor]
        st.dataframe(filtered)
        st.markdown("---")
        if filtered:
            selected_sale = st.selectbox(
                "Seleccionar venta para borrar",
                [f"{idx + 1} - {sale['Date']} - {sale['Client']} - {sale['Package']}" for idx, sale in enumerate(filtered)],
            )
            if selected_sale:
                delete_index = int(selected_sale.split(" - ")[0]) - 1
                sale_to_delete = filtered[delete_index]
                if st.button("Borrar venta seleccionada"):
                    sales.remove(sale_to_delete)
                    save_sales(sales)
                    st.success("Venta borrada.")
                    st.rerun()
        csv_data = "Date,Client,Advisor,Package,Destination,Cruise,Hotel,Commission,Follow-up status\n"
        for row in filtered:
            csv_data += ",".join([row[k].replace(",", ";") for k in ["Date", "Client", "Advisor", "Package", "Destination", "Cruise", "Hotel", "Commission", "Follow-up status"]]) + "\n"
        st.download_button("Export CSV", csv_data, file_name="sales_history.csv", mime="text/csv")
    else:
        st.info("No hay ventas registradas aún.")


def permissions_page():
    st.title(tr("permissions"))
    matrix = config.get("permission_matrix", DEFAULT_CONFIG["permission_matrix"])
    st.markdown("### Permission examples")
    table = []
    for perm_key, values in matrix.items():
        table.append({
            "Permission": PERMISSION_DESCRIPTIONS.get(perm_key, perm_key),
            "Advisor": values.get("advisor"),
            "Admin": values.get("admin"),
        })
    st.dataframe(table)


# -----------------------------------
# PÁGINAS ADVISOR
# -----------------------------------

def advisor_home():
    st.title(tr("home"))
    st.metric("Daily sales", summary["sales_today"])
    st.metric("Pending follow-ups", summary["pending_followups"])
    st.metric("Personal commission", format_money(summary["advisor_commission"]))
    st.markdown("---")
    st.subheader("Latest clients")
    my_clients = [c for c in clients if c["Assigned advisor"] == name]
    st.dataframe(my_clients[-5:])


def new_client_page():
    st.title(tr("new_client"))
    with st.form("new_client"):
        full_name = st.text_input(tr("full_name"))
        state = st.text_input(tr("state"))
        age = st.number_input(tr("age"), min_value=18, max_value=100, value=30)
        marital_status = st.selectbox(tr("marital_status"), ["Casado / Convive", "Mujer Soltera", "Hombre Soltero"])
        residency = st.selectbox(tr("residency"), ["Sí", "No"])
        children_count = st.number_input(tr("children_count"), min_value=0, max_value=10, value=0)
        children_ages = st.text_input(tr("children_ages"))
        interest = st.selectbox("Interest level", ["High", "Medium", "Low"])
        preferred_package = st.selectbox("Preferred package", ["VDL", "HÍBRIDO", "MIX & MATCH"])
        if st.form_submit_button(tr("save_client")):
            qualification = calculate_qualification({
                "Residency": residency,
                "Marital status": marital_status,
                "Age": age,
                "Children ages": children_ages,
            })
            package = preferred_package if qualification == preferred_package else qualification
            if package == "No qualify":
                package = "MIX & MATCH"
            destination = "Cancún" if package == "VDL" else "Las Vegas" if package == "HÍBRIDO" else "Bahamas"
            client_id = str(len(clients) + 1)
            clients.append({
                "ID": client_id,
                "Full name": full_name,
                "State": state,
                "Age": str(age),
                "Marital status": marital_status,
                "Residency": residency,
                "Children count": str(children_count),
                "Children ages": children_ages,
                "Assigned advisor": name,
                "Qualification result": qualification,
                "Package": package,
                "Destination": destination,
                "Follow-up status": "Interested",
                "Notes": f"Interest: {interest}",
                "Registration date": today_str(),
            })
            save_clients(clients)
            st.success("Cliente registrado.")
            if qualification != "No qualify":
                st.success(f"Califica para {qualification}.")
            else:
                st.warning("No califica para VDL / HÍBRIDO. Enviar a MIX & MATCH.")
            st.rerun()


def registered_clients_page():
    st.title(tr("registered_clients"))
    my_clients = [c for c in clients if c["Assigned advisor"] == name]
    search_name = st.text_input("Buscar cliente")
    if search_name:
        my_clients = [c for c in my_clients if search_name.lower() in c["Full name"].lower()]
    st.dataframe(my_clients)
    st.markdown("---")
    st.subheader("Update status or add notes")
    client_ids = [c["ID"] for c in my_clients]
    if client_ids:
        selected_id = st.selectbox("Select client", client_ids)
        client = next((c for c in my_clients if c["ID"] == selected_id), None)
        if client:
            new_status = st.selectbox("Follow-up status", config["follow_up_status"], index=config["follow_up_status"].index(client["Follow-up status"]) if client["Follow-up status"] in config["follow_up_status"] else 0)
            new_note = st.text_area("Add note")
            if st.button("Guardar cambios"):
                client["Follow-up status"] = new_status
                if new_note:
                    client["Notes"] = client["Notes"] + "\n" + new_note if client["Notes"] else new_note
                save_clients(clients)
                st.success("Cliente actualizado.")
                st.rerun()
    else:
        st.info("No tienes clientes registrados aún.")


def destinations_cruises_page():
    st.title(tr("destinations_cruises"))
    st.markdown("### Destinations")
    for city, hotel_list in hotels_and_cruises["hoteles"].items():
        st.write(f"**{city}**")
        for hotel in hotel_list:
            st.write(f"- {hotel}")
    st.markdown("---")
    st.markdown("### Cruises")
    for category, cruise_list in hotels_and_cruises["cruises"].items():
        st.write(f"**{category}**")
        for cruise in cruise_list:
            st.write(f"- {cruise['departure']} → {cruise['route']}")


def package_qualification_page():
    st.title(tr("package_qualification"))
    with st.form("qualification_form"):
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        marital_status = st.selectbox("Marital status", ["Casado / Convive", "Mujer Soltera", "Hombre Soltero"])
        residency = st.selectbox("Residency", ["Sí", "No"])
        children_ages = st.text_input("Children ages (comma separated)")
        if st.form_submit_button("Calcular calificación"):
            qualification = calculate_qualification({
                "Residency": residency,
                "Marital status": marital_status,
                "Age": age,
                "Children ages": children_ages,
            })
            if qualification == "No qualify":
                st.warning("No califica para VDL / HÍBRIDO. Enviar a MIX & MATCH.")
            else:
                st.success(f"Califica para {qualification}.")
            if qualification == "VDL":
                st.write("Destinations: Cancun, Punta Cana, Puerto Vallarta, Los Cabos, Costa Rica, Bahamas")
            elif qualification == "HÍBRIDO":
                st.write("Destinations: Cancun, Las Vegas, Orlando")
            else:
                st.write("Destinations: USA, Canada, Bahamas, Mexico")


        def calificaciones_page():
            st.title(tr("calificaciones"))
            st.markdown("""
            **CALIFICACIONES: QMG - VIAJE DE LUJO EFECTIVO DICIEMBRE /01/2021**

            **AREA ESTE DE USA**

            **ORLANDO (4/3): 4 PERSONAS**
            - PAREJAS CASADAS O CONVIVAN MAYORES DE 25-79 AÑOS (UNO DE ELLOS EDAD REQUERIDA)
            - MUJERES SOLTERAS MAYORES DE 25-65 AÑOS

            **SOUTH FLORIDA (4/3): 4 PERSONAS**
            - PAREJAS CASADAS O CONVIVAN MAYORES DE 25-75 AÑOS (UNO DE ELLOS EDAD REQUERIDA)
            - MUJERES SOLTERAS MAYORES DE 25-72 AÑOS

            **DAYTONA (4/3): 4 PERSONAS**
            - PAREJAS CASADAS O CONVIVAN MAYORES DE 25-72 AÑOS (AMBOS EDAD REQUERIDA)

            **HILTON HEAD, SC (3/2): 4 PERSONAS**
            - PAREJAS CASADAS O CONVIVAN MAYORES DE 26-75 AÑOS (AMBOS EDAD REQUERIDA)

            **VIRGINIA BEACH, VA (3/2): 4 PERSONAS**
            - PAREJAS CASADAS MAYORES DE 25-75 AÑOS (AMBOS ENTRE ESTAS EDADES)

            **AREA OESTE DE USA**

            **LAS VEGAS (4/3): 2 PERSONAS**
            - PAREJAS CASADAS O CONVIVAN MAYORES DE 25-72 AÑOS (UNO DE ELLOS EDAD REQUERIDA)
            - MUJERES SOLTERAS MAYORES DE 25-65 AÑOS

            **LAKE HAVASU, AZ (4/3): 4 PERSONAS**
            - PAREJAS CASADAS O CONVIVAN MAYORES DE 25-70 AÑOS (UNO DE ELLOS EDAD REQUERIDA)
            - MUJERES SOLTERAS MAYORES DE 35-70 AÑOS

            **AREA CENTRO NORTE DE USA**

            **PEQUOT LAKES, MN (3/2): 4 PERSONAS**
            - PAREJAS CASADAS O CONVIVAN MAYORES DE 28-70 AÑOS (AMBOS EDAD REQUERIDA)
            - MUJERES SOLTERAS MAYORES DE 18-70 AÑOS

            **BRANSON, MO (4/3): 4 PERSONAS**
            - PAREJAS CASADAS O CONVIVAN MAYORES DE 28-75 AÑOS (AMBOS EDAD REQUERIDA)

            **DESTINOS INTERNACIONALES EFECTIVO DICIEMBRE /01/2021**

            **PUNTA CANA (5/4): 2 ADULTOS Y 2 NIÑOS (MENORES DE 11 AÑOS) (US CIT. ONLY)**
            - PAREJAS CASADAS O CONVIVAN MAYORES DE 30-65 AÑOS (UNO DE ELLOS EDAD REQUERIDA)

            **CANCÚN (5/4): 2 ADULTOS Y 2 NIÑOS (MENORES DE 11 AÑOS) - TRANS. AEROPUERTO-HOTEL - ALL INCLUSIVE**
            - PAREJAS CASADAS O CONVIVAN ENTRE LAS EDADES DE 30-70 AÑOS (AMBOS EDAD REQUERIDA)
            - MUJERES SOLTERAS MAYORES DE 30-70 AÑOS
            - HOMBRES SOLTEROS MAYORES DE 30-70 AÑOS

            **PUERTO VALLARTA (5/4): 2 ADULTOS Y 2 NIÑOS (MENORES DE 11 AÑOS) - TRANS. AEROPUERTO-HOTEL - ALL INCLUSIVE**
            - PAREJAS CASADAS ENTRE LAS EDADES DE 30-70 AÑOS (AMBOS EDAD REQUERIDA)
            - MUJERES SOLTERAS MAYORES DE 30-70 AÑOS
            - HOMBRES SOLTEROS MAYORES DE 35-59 AÑOS

            **LOS CABOS (5/4): 2 ADULTOS Y 2 NIÑOS (MENORES DE 11 AÑOS) - TRANS. AEROPUERTO-HOTEL - ALL INCLUSIVE**
            - PAREJAS CASADAS ENTRE LAS EDADES DE 30-70 AÑOS (AMBOS EDAD REQUERIDA)
            - MUJERES SOLTERAS MAYORES DE 30-70 AÑOS
            - HOMBRES SOLTEROS MAYORES DE 35-59 AÑOS

            **BAHAMAS (4/3): 4 ADULTOS (SOLO HOTEL)**
            - PAREJAS CASADAS O CONVIVAN ENTRE LAS EDADES DE 28-68 AÑOS (AMBOS EDAD REQUERIDA)
            - MUJERES SOLTERAS MAYORES DE 28-68 AÑOS

            **COSTA RICA (5/4): 2 ADULTOS - TRANSPORTACIÓN AEROPUERTO-HOTEL-AEROPUERTO - ALL INCLUSIVE**
            - PAREJAS CASADAS O CONVIVAN ENTRE LAS EDADES DE 30-70 AÑOS (UNO DE ELLOS EDAD REQUERIDA)
            - MUJERES SOLTERAS MAYORES DE 35-70 AÑOS
            """, unsafe_allow_html=False)


def my_commissions_page():
    st.title(tr("my_commissions"))
    advisor_sales = [s for s in sales if s["Advisor"] == name]
    daily = sum(1 for s in advisor_sales if s["Date"].startswith(today_str()))
    weekly = sum(1 for s in advisor_sales if datetime.strptime(s["Date"], "%Y-%m-%d %H:%M:%S").isocalendar()[1] == datetime.now().isocalendar()[1]) if advisor_sales else 0
    monthly = sum(1 for s in advisor_sales if s["Date"][0:7] == today_str()[0:7])
    total = sum(float(s.get("Commission", 0) or 0) for s in advisor_sales)
    st.metric("Daily commission", format_money(sum(float(s.get("Commission", 0) or 0) for s in advisor_sales if s["Date"].startswith(today_str()))))
    st.metric("Weekly commission", format_money(sum(float(s.get("Commission", 0) or 0) for s in advisor_sales if datetime.strptime(s["Date"], "%Y-%m-%d %H:%M:%S").isocalendar()[1] == datetime.now().isocalendar()[1])))
    st.metric("Monthly commission", format_money(sum(float(s.get("Commission", 0) or 0) for s in advisor_sales if s["Date"][0:7] == today_str()[0:7])))
    st.metric("Total earnings", format_money(total))
    st.metric("Sales count", len(advisor_sales))
    st.metric("Commission percentage", f"{int(config.get('porcentaje_default', 0.06)*100)}%")
    st.markdown("---")
    st.dataframe(advisor_sales)


def my_statistics_page():
    st.title(tr("my_statistics"))
    my_clients = [c for c in clients if c["Assigned advisor"] == name]
    total_clients = len(my_clients)
    closed_sales = sum(1 for c in my_clients if c["Follow-up status"] == "Closed sale")
    lost_clients = sum(1 for c in my_clients if c["Follow-up status"] == "No answer")
    best_destination = "N/A"
    destination_counts = {}
    for c in my_clients:
        destination_counts[c["Destination"]] = destination_counts.get(c["Destination"], 0) + 1
    if destination_counts:
        best_destination = max(destination_counts, key=destination_counts.get)
    st.metric("Registered clients", total_clients)
    st.metric("Closed sales", closed_sales)
    st.metric("Lost clients", lost_clients)
    st.metric("Best destination", best_destination)
    st.markdown("---")
    st.bar_chart(destination_counts)


def followups_page():
    st.title(tr("followups"))
    follow_up_clients = [c for c in clients if c["Assigned advisor"] == name and c["Follow-up status"] in ["Pending call", "Follow-up"]]
    if follow_up_clients:
        st.dataframe(follow_up_clients)
    else:
        st.info("No pending follow-ups.")
    st.markdown("---")
    st.subheader("Update follow-up")
    ids = [c["ID"] for c in follow_up_clients]
    if ids:
        selected = st.selectbox("Seleccionar cliente", ids)
        client = next((c for c in follow_up_clients if c["ID"] == selected), None)
        if client:
            new_status = st.selectbox("Nuevo estado", config["follow_up_status"], index=config["follow_up_status"].index(client["Follow-up status"]))
            note = st.text_area("Agregar nota")
            if st.button("Guardar seguimiento"):
                client["Follow-up status"] = new_status
                if note:
                    client["Notes"] += "\n" + note if client["Notes"] else note
                save_clients(clients)
                st.success("Seguimiento actualizado.")
                st.rerun()


def my_profile_page():
    st.title(tr("my_profile"))
    user = get_user(username, users)
    st.write(f"**{tr('usuario')}:** {user['Usuario']}")
    st.write(f"**{tr('full_name')}:** {user['Name']}")
    st.write(f"**Rol:** {user['Rol']}")
    with st.form("profile_form"):
        new_password = st.text_input("Nueva contraseña", type="password")
        if st.form_submit_button("Actualizar contraseña"):
            if new_password:
                user["Password"] = new_password
                save_users(users)
                st.success("Contraseña actualizada.")
            else:
                st.error("Ingresa una nueva contraseña.")

    st.markdown("---")
    st.subheader(tr('work_schedules'))
    new_schedules = {}
    for zona, hora in config['horarios'].items():
        new_schedules[zona] = st.text_input(f"Horario {zona}", value=hora, key=f"hora_{zona}")
    st.subheader(tr('zones'))
    zones_text = st.text_area("Mapa de zonas (estado: zona)", value=json.dumps(config['zones'], ensure_ascii=False, indent=2), height=220)
    st.subheader(tr('commission_percentage'))
    percentage_default = st.number_input("Porcentaje (%)", 0.0, 100.0, value=config.get('porcentaje_default', 0.06) * 100)
    if st.button(tr('save_config')):
        try:
            config['zones'] = json.loads(zones_text)
            config['horarios'] = new_schedules
            config['porcentaje_default'] = percentage_default / 100
            save_json(CONFIG_FILE, config)
            st.success(tr('config_saved'))
        except json.JSONDecodeError:
            st.error(tr('zones_invalid'))


# -----------------------------------
# RUTEO PRINCIPAL
# -----------------------------------

if role == "admin":
    if page == "dashboard":
        dashboard_page()
    elif page == "users":
        users_page()
    elif page == "clients":
        clients_page()
    elif page == "sales":
        sales_page()
    elif page == "hotels_cruises":
        hotels_cruises_page()
    elif page == "packages":
        packages_page()
    elif page == "commissions":
        commissions_page()
    elif page == "statistics":
        statistics_page()
    elif page == "sales_history":
        sales_history_page(is_admin=True)
    elif page == "home":
        advisor_home()
    elif page == "new_client":
        new_client_page()
    elif page == "registered_clients":
        registered_clients_page()
    elif page == "destinations_cruises":
        destinations_cruises_page()
    elif page == "package_qualification":
        package_qualification_page()
    elif page == "my_commissions":
        my_commissions_page()
    elif page == "my_statistics":
        my_statistics_page()
    elif page == "followups":
        followups_page()
    elif page == "my_profile":
        my_profile_page()
else:
    if page == "home":
        advisor_home()
    elif page == "new_client":
        new_client_page()
    elif page == "sales":
        sales_page()
    elif page == "registered_clients":
        registered_clients_page()
    elif page == "destinations_cruises":
        destinations_cruises_page()
    elif page == "package_qualification":
        package_qualification_page()
    elif page == "my_commissions":
        my_commissions_page()
    elif page == "my_statistics":
        my_statistics_page()
    elif page == "followups":
        followups_page()
    elif page == "sales_history":
        sales_history_page(is_admin=False)
    elif page == "my_profile":
        my_profile_page()
        