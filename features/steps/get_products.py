from client.retrieve import Retrieve

@when('retrieve all products')
def step_impl(context):
  get = Retrieve()
  context.response = get.retrieve_all()

@then('check products')
def step_impl(context):
  assert context.response.status_code == 200
  assert context.response.json()[0]['id']
  assert context.response.json()[0]['nome']
  assert context.response.json()[0]['descricao']
  assert context.response.json()[0]['preco']
