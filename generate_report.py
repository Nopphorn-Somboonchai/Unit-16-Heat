def round_half_even(num, decimals=0):
    multiplier = 10 ** decimals
    return round(num * multiplier) / multiplier

def run_tests_for_r(R):
    results = []

    # 1. 16_1_1_q2_celsius_to_kelvin
    t = round_half_even(-150 + (R * 13.5), 2)
    T_kelvin = t + 273.15
    results.append({"id": "16_1_1_q2", "params": f"t = {t}", "answers": [f"{T_kelvin:.2f}"]})

    # 2. 16_1_1_q3_kelvin_to_celsius
    T = round_half_even(5 + (R * 14.2), 2)
    t_celsius = T - 273.15
    results.append({"id": "16_1_1_q3", "params": f"T = {T}", "answers": [f"{t_celsius:.2f}"]})

    # 3. 16_1_2_q2_metal_specific_heat
    m = round_half_even(1.0 + (R * 0.1), 1)
    Q = round(1000 + (R * 200))
    T1 = round(15 + (R % 15))
    dT = round(10 + (R % 30))
    C = Q / dT
    c = C / m
    results.append({"id": "16_1_2_q2", "params": f"m = {m}, Q = {Q}, T1 = {T1}, dT = {dT}", "answers": [f"{C:.1f}", f"{c:.1f}"]})

    # 4. 16_1_2_q5_pool_heat
    m_pool = round_half_even(0.5 + (R * 0.05), 2) * 1e6
    dT_pool = round(1 + (R % 4))
    Q_pool = m_pool * 4186 * dT_pool
    results.append({"id": "16_1_2_q5", "params": f"m = {m_pool:e}, dT = {dT_pool}", "answers": [f"{Q_pool:e}"]})

    # 5. 16_1_3_q1_ice_melting_heat
    m_ice = round_half_even(0.5 + (R * 0.2), 1)
    Q_ice = m_ice * 3.33e5
    Q_ice_kJ = Q_ice / 1000
    results.append({"id": "16_1_3_q1", "params": f"m = {m_ice}", "answers": [f"{Q_ice_kJ:.1f}"]})

    # 6. 16_1_3_q2_ice_to_steam
    m_steam = round_half_even(0.1 + (R * 0.07), 2)
    Q_tot = m_steam * 4186 * 100 + m_steam * 22.56e5
    Q_tot_kJ = Q_tot / 1000
    results.append({"id": "16_1_3_q2", "params": f"m = {m_steam}", "answers": [f"{Q_tot_kJ:.1f}"]})

    # 7. 16_1_3_q5_ice_to_steam_full
    m_full = round_half_even(0.5 + (R * 0.06), 1)
    T_start = -round(2 + (R % 18))
    Q1 = m_full * 2100 * abs(T_start)
    Q2 = m_full * 3.33e5
    Q3 = m_full * 4186 * 100
    Q4 = m_full * 22.56e5
    Q_total_MJ = (Q1 + Q2 + Q3 + Q4) / 1e6
    results.append({"id": "16_1_3_q5", "params": f"m = {m_full}, T_start = {T_start}", "answers": [f"{Q_total_MJ:.2f}"]})

    # 8. 16_1_4_q3_metal_in_ice_calculation
    m1 = round(100 + (R * 10))
    T_metal = round(200 + (R * 6))
    m2 = round(100 + (R * 8))
    T_final = round_half_even(2.0 + (R * 0.2), 1)
    Q_gain = (m2 / 1000) * 3.33e5 + (m2 / 1000) * 4186 * T_final
    c_metal = Q_gain / ((m1 / 1000) * (T_metal - T_final))
    results.append({"id": "16_1_4_q3", "params": f"m1={m1}, T_metal={T_metal}, m2={m2}, T_final={T_final}", "answers": [f"{Q_gain:.0f}", f"{c_metal:.1f}"]})

    return results

def main():
    rolls = [1, 15, 40]
    md = "# Dynamic Quiz Verification Results\n\n"
    md += "This report verifies the dynamically generated questions and their correct answers for students with Roll Numbers 1, 15, and 40.\n\n"
    
    for r in rolls:
        md += f"## Roll Number (R) = {r}\n"
        md += "| Question ID | Generated Parameters | Computed Expected Answer |\n"
        md += "|---|---|---|\n"
        results = run_tests_for_r(r)
        for res in results:
            answers_str = " , ".join(res['answers'])
            md += f"| `{res['id']}` | `{res['params']}` | `{answers_str}` |\n"
        md += "\n"
        
    with open('exam_verification.md', 'w', encoding='utf-8') as f:
        f.write(md)
    print("exam_verification.md created")

if __name__ == '__main__':
    main()
