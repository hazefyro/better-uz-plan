MOCK_SCHEDULE_HTML = """
<table id="table_details" class="table table-bordered table-condensed">
    <tbody>
        <tr class="gray">
            <th width="10%">Termin</th>
            <th width="5%">Dzień</th>
            <th width="2%">PG</th>
            <th align="center" width="2%">Od</th>
            <th align="center" width="2%">Do</th>
            <th width="30%">Przedmiot</th>
            <th width="4%">RZ</th>
            <th width="25%">Nauczyciel</th>
            <th width="15%">Miejsce</th>
        </tr>

        <tr class="even day3 rzD">
            <td>2026-03-04</td>
            <td>Śr</td>
            <td class="PG">&nbsp;</td>
            <td align="center">09:15</td>
            <td align="center">10:45</td>
            <td>
                Podstawy informatyki II
                <a href="https://classroom.google.com/c/ODQ3MzU2MzU4OTEz"
                    ><img
                        data-bs-toggle="tooltip"
                        data-bs-html="true"
                        data-bs-placement="top"
                        src="img/link-classroom.png"
                        aria-label="Google Classroom"
                        data-bs-original-title="Google Classroom"
                /></a>
            </td>
            <td>
                <label
                    data-bs-toggle="tooltip"
                    data-bs-html="true"
                    data-bs-placement="top"
                    class="rz"
                    data-bs-original-title="Ć - Ćwiczenia"
                    >Ć</label
                >
            </td>
            <td>
                <a href="nauczyciel_plan.php?ID=40132"
                    >dr hab. inż. Piotr Borowiecki, prof. UZ</a
                >
            </td>
            <td>
                <i
                    data-bs-toggle="tooltip"
                    data-bs-html="true"
                    data-bs-placement="top"
                    class="bi bi-buildings"
                    aria-label="Zajęcia bezpośrednie"
                    data-bs-original-title="Zajęcia bezpośrednie"
                ></i>
                <a href="sale_plan.php?ID=450715">110/111 A-2</a>
            </td>
        </tr>

        <tr class="odd day3 rzD">
            <td>2026-03-04</td>
            <td>Śr</td>
            <td class="PG">&nbsp;</td>
            <td align="center">12:45</td>
            <td align="center">14:15</td>
            <td>
                Podstawy analizy danych
                <a href="https://classroom.google.com/c/ODQ3MDMyNDc2MDI2"
                    ><img
                        data-bs-toggle="tooltip"
                        data-bs-html="true"
                        data-bs-placement="top"
                        src="img/link-classroom.png"
                        aria-label="Google Classroom"
                        data-bs-original-title="Google Classroom"
                /></a>
            </td>
            <td>
                <label
                    data-bs-toggle="tooltip"
                    data-bs-html="true"
                    data-bs-placement="top"
                    class="rz"
                    data-bs-original-title="W - Wykład"
                    >W</label
                >
            </td>
            <td>
                <a href="nauczyciel_plan.php?ID=12209"
                    >prof. dr hab. inż. Dariusz Uciński</a
                >
            </td>
            <td>
                <i
                    data-bs-toggle="tooltip"
                    data-bs-html="true"
                    data-bs-placement="top"
                    class="bi bi-buildings"
                    aria-label="Zajęcia bezpośrednie"
                    data-bs-original-title="Zajęcia bezpośrednie"
                ></i>
                <a href="sale_plan.php?ID=4759">H044 A-10</a>
            </td>
        </tr>

        <tr class="even day3 rzD">
            <td>2026-03-04</td>
            <td>Śr</td>
            <td class="PG">&nbsp;</td>
            <td align="center">14:30</td>
            <td align="center">15:55</td>
            <td>Fizyka</td>
            <td>
                <label
                    data-bs-toggle="tooltip"
                    data-bs-html="true"
                    data-bs-placement="top"
                    class="rz"
                    data-bs-original-title="W - Wykład"
                    >W</label
                >
            </td>
            <td>
                <a href="nauczyciel_plan.php?ID=672">dr Stefan Jerzyniak</a>
            </td>
            <td>
                <i
                    data-bs-toggle="tooltip"
                    data-bs-html="true"
                    data-bs-placement="top"
                    class="bi bi-buildings"
                    aria-label="Zajęcia bezpośrednie"
                    data-bs-original-title="Zajęcia bezpośrednie"
                ></i>
                <a href="sale_plan.php?ID=1095">106 A-29</a>
            </td>
        </tr>
    </tbody>
</table>
"""

MOCK_GROUP_HTML = """
<TABLE class="table table-bordered table-condensed">
      <TR class="odd"><td><a href="grupy_plan.php?ID=30551">11INF-SD(L) Informatyka / stacjonarne / drugiego stopnia z tyt. magistra inżyniera</a></td></tr>
      <TR class="even"><td><a href="grupy_plan.php?ID=30552">11INF-SP Informatyka / stacjonarne / pierwszego stopnia z tyt. inżyniera</a></td></tr>
      <TR class="odd"><td><a href="grupy_plan.php?ID=30553">12INF-SD(L) Informatyka / stacjonarne / drugiego stopnia z tyt. magistra inżyniera</a></td></tr>
      <TR class="even"><td><a href="grupy_plan.php?ID=30554">12INF-SP Informatyka / stacjonarne / pierwszego stopnia z tyt. inżyniera</a></td></tr>
      <TR class="odd"><td><a href="grupy_plan.php?ID=30555">13INF-SP Informatyka / stacjonarne / pierwszego stopnia z tyt. inżyniera</a></td></tr>
</TABLE>
"""

INVALID_MOCK_GROUP_HTML = """
<TABLE class="table table-bordered table-condensed">
      <TR class="odd"><td><a href="">11INF-SD(L) Informatyka / stacjonarne / drugiego stopnia z tyt. magistra inżyniera</a></td></tr>
      <TR class="even"><td><a href="grupy_plan.php?ID=30552">11INF-SP Informatyka / stacjonarne / pierwszego stopnia z tyt. inżyniera</a></td></tr>
      <TR class="odd"><td><a href="grupy_plan.php?ID=30553">12INF-SD(L) Informatyka / stacjonarne / drugiego stopnia z tyt. magistra inżyniera</a></td></tr>
      <TR class="even"><td><a href="grupy_plan.php?ID=30554">12INF-SP Informatyka / stacjonarne / pierwszego stopnia z tyt. inżyniera</a></td></tr>
      <TR class="odd"><td><a href="grupy_plan.php?ID=30555">13INF-SP Informatyka / stacjonarne / pierwszego stopnia z tyt. inżyniera</a></td></tr>
</TABLE>
"""

INVALID_MOCK_SCHEDULE = """
<table id="table_details" class="table table-bordered table-condensed">
    <tbody>
        <tr class="gray">
            <th width="10%">Termin</th>
            <th width="5%">Dzień</th>
            <th width="2%">PG</th>
            <th align="center" width="2%">Od</th>
            <th align="center" width="2%">Do</th>
            <th width="30%">Przedmiot</th>
            <th width="4%">RZ</th>
            <th width="25%">Nauczyciel</th>
            <th width="15%">Miejsce</th>
        </tr>

        <tr class="even day3 rzD">
            <td>2026-03-04</td>
            <td>Śr</td>
            <td class="PG">&nbsp;</td>
            <td align="center">bad_time</td>
            <td align="center">10:45</td>
            <td>
                Podstawy informatyki II
                <a href="https://classroom.google.com/c/ODQ3MzU2MzU4OTEz"
                    ><img
                        data-bs-toggle="tooltip"
                        data-bs-html="true"
                        data-bs-placement="top"
                        src="img/link-classroom.png"
                        aria-label="Google Classroom"
                        data-bs-original-title="Google Classroom"
                /></a>
            </td>
            <td>
                <label
                    data-bs-toggle="tooltip"
                    data-bs-html="true"
                    data-bs-placement="top"
                    class="rz"
                    data-bs-original-title="Ć - Ćwiczenia"
                    ></label
                >
            </td>
            <td>
                <a href="nauczyciel_plan.php?ID=40132"
                    >dr hab. inż. Piotr Borowiecki, prof. UZ</a
                >
            </td>
            <td>
                <i
                    data-bs-toggle="tooltip"
                    data-bs-html="true"
                    data-bs-placement="top"
                    class="bi bi-buildings"
                    aria-label="Zajęcia bezpośrednie"
                    data-bs-original-title="Zajęcia bezpośrednie"
                ></i>
                <a href="sale_plan.php?ID=450715">110/111 A-2</a>
            </td>
        </tr>

    </tbody>
</table>
"""
