#  Considere a seguinte situação: descontam-se inicialmente 10% do salário bruto do trabalhador como contribuição à previdência social. Após esse desconto, há um outro desconto de 5% sobre o valor restante do salário bruto, a título de um determinado imposto. Faça um programa que leia o salário bruto de um cidadão e imprima o seu salário líquido.

# Solicitar Valor Salário Bruto 
#%%

salario_bruto = float(input('Digite o valor do salário bruto R$ :'))
salario_bruto
# %%
# Calcular desconto previdenciario de 10% sob salário bruto
desconto_previdenciario = salario_bruto * 0.10
saldo_apos_desconto_previdenciario = salario_bruto - desconto_previdenciario

saldo_apos_desconto_previdenciario
#%%
# Calcular desconto de imposto de 05% sob saldo do salário após desconto previdenciario
desconto_imposto = saldo_apos_desconto_previdenciario * 0.05
salario_liquido = saldo_apos_desconto_previdenciario - desconto_imposto
salario_liquido
#%%
# Exibir salário bruto e líquido
print(f'Salário Bruto: R$ {salario_bruto: .2f}, Salário Líquido: R${salario_liquido: .2f}')

# %%
