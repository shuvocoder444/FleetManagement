new_keys_en = {
    'menu_buy_subscription': 'Buy Subscription',
    'purchase_sub_title': 'Purchase Subscription',
    'purchase_sub_desc': 'Select your preferred subscription plan and submit manual payment details (Bank Transfer, Cash, or Mobile Wallet) for instant activation.',
    'sub_billing_badge': 'Subscription Billing',
    'direct_payment_activation': 'Direct Payment & Activation',
    'my_subscriptions_btn': 'My Subscriptions',
    'step_1_choose_plan': 'Choose Your Plan',
    'step_2_instructions': 'Payment Instructions',
    'payable_amount': 'Payable Amount',
    'bank_transfer_details': 'Bank Transfer Details',
    'bank_name_label': 'Bank:',
    'account_name_label': 'Account Name:',
    'account_no_label': 'Account No:',
    'swift_label': 'SWIFT:',
    'mobile_wallet_cash': 'Mobile Wallet / Cash',
    'payment_ref_label': 'Payment Ref:',
    'after_payment_notice': 'After completing payment via your banking app or cash, please fill out the confirmation form on the right.',
    'step_3_submit_details': 'Submit Payment Details',
    'chosen_plan_label': 'Chosen Plan',
    'payment_method_used': 'Payment Method Used',
    'method_bank_transfer': 'Bank Transfer (DKIB / Wire)',
    'method_cash': 'Cash Deposit / Office Handover',
    'trx_ref_label': 'Transaction Reference / TrxID / Slip Number',
    'trx_ref_placeholder': 'e.g. TXN-98421038 or DemirBank Ref #49302',
    'trx_ref_help': 'Enter the unique transaction code, bank reference ID, or payer name from your payment receipt.',
    'purchasing_account_label': 'Purchasing Account',
    'confirm_payment_btn': 'Confirm & Submit Manual Payment',
    'verification_notice': 'Your payment will be verified by the admin team within 15–30 minutes.',
}

new_keys_ru = {
    'menu_buy_subscription': 'Купить подписку',
    'purchase_sub_title': 'Оформление подписки',
    'purchase_sub_desc': 'Выберите подходящий тарифный план и отправьте данные об оплате (банковский перевод, наличные или мобильный кошелек) для быстрой активации.',
    'sub_billing_badge': 'Биллинг и подписка',
    'direct_payment_activation': 'Прямая оплата и активация',
    'my_subscriptions_btn': 'Мои подписки',
    'step_1_choose_plan': 'Выберите ваш тариф',
    'step_2_instructions': 'Инструкции по оплате',
    'payable_amount': 'Сумма к оплате',
    'bank_transfer_details': 'Реквизиты для банковского перевода',
    'bank_name_label': 'Банк:',
    'account_name_label': 'Получатель:',
    'account_no_label': 'Расчетный счет:',
    'swift_label': 'SWIFT:',
    'mobile_wallet_cash': 'Мобильный кошелек / Наличные',
    'payment_ref_label': 'Назначение платежа:',
    'after_payment_notice': 'После совершения оплаты через банковское приложение или наличными, заполните форму подтверждения справа.',
    'step_3_submit_details': 'Отправка данных об оплате',
    'chosen_plan_label': 'Выбранный тариф',
    'payment_method_used': 'Способ оплаты',
    'method_bank_transfer': 'Банковский перевод (DKIB / Реквизиты)',
    'method_cash': 'Оплата наличными в офисе',
    'trx_ref_label': 'Номер транзакции / Код квитанции / TrxID',
    'trx_ref_placeholder': 'например, TXN-98421038 или DemirBank #49302',
    'trx_ref_help': 'Введите номер перевода, ID чека или имя плательщика из банковской квитанции.',
    'purchasing_account_label': 'Аккаунт плательщика',
    'confirm_payment_btn': 'Подтвердить и отправить данные оплаты',
    'verification_notice': 'Ваш платеж будет проверен и активирован администрацией в течение 15–30 минут.',
}

with open('apps/site_settings/translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert into EN section
en_target = "'subscriptions_title': 'Subscriptions & Memberships',"
assert en_target in content, "en_target not found!"

en_insert = "\n" + "\n".join([f"              {k!r}: {v!r}," for k, v in new_keys_en.items()])
content = content.replace(en_target, en_target + en_insert, 1)

# Insert into RU section
ru_target = "'subscriptions_title': 'Подписки и тарифы',"
assert ru_target in content, "ru_target not found!"

ru_insert = "\n" + "\n".join([f"              {k!r}: {v!r}," for k, v in new_keys_ru.items()])
content = content.replace(ru_target, ru_target + ru_insert, 1)

with open('apps/site_settings/translations.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully added billing purchase translations to translations.py")
