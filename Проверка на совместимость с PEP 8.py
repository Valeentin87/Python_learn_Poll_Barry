# существует единый стандарт написания кода на Python именуемый PEP 8
# покажем как можно проверить свой код на совместимость с PEP 8 путем прохождения pytest
# 1. Необходимо в командной строке от имени администратора установить pytest и pep8, набрав команды
                py -3 -m pip install pytest
                py -3 -m pip install pytest-pep8
                
# 2. Далее в терминале непосредственно из того каталога, где находится проверяемый файл набираем:
                py.test --pep8 vsearch.py (имя проверяемого файла)
                либо
                pycodestyle controller.py
# при этом увидим перечень не соответствий

