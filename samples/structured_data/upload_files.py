from st_library.structured_data import Table

from st_library import Library
st_lib = Library()
st_lib.set_token('Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4MTIyYTNkMy1lZmQ2LTQwMjYtOGVlZi04MzMzNmJlNmFkNzciLCJpc3MiOiJzaG9ydGVzdHRyYWNrLXVhYSIsImF1dGhvcml0aWVzIjpbIlJPTEVfQ09NUEFOWV9BRE1JTiJdLCJkamFuZ29Vc2VySWQiOiI5OTkiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwiYXVkIjoid2ViX2FwcCIsImNvbXBhbnlJZCI6InRlc3Rfc2hvcnRlc3R0cmFja19mdW5jdGlvbmFsaXR5IiwiZGphbmdvVG9rZW4iOiI5NjUxYmQzZGJiZWExZDQ5YjM1MzhjZjRjMDU1MWMzODhiOGVlNzZlIiwic2NvcGUiOlsib3BlbmlkIl0sImV4cCI6MTUxNjgzMjY5NiwiaWF0IjoxNTE2NTMyNjk2LCJqdGkiOiJiOTc2OTQzYi1iODFjLTQ5Y2QtOTUwNS1hYzEyNTU0NWI5YWIiLCJlbWFpbCI6InB1YmxpYy1hZG1pbkBsb2NhbGhvc3QifQ.Gv1tC5XXicxg3YlTrYnUSBQ1kqqXixCCIFdh60qINSD4IatHIQcYJQGeWQX80HBO2bHbgF7lLuKywf03KkQRO0n6yQnPmTcLHk1JBk74FZ-vY0upvxA4b5TjlYNod1kZwPNwIg2icc-g-hDJfX38R6-CRaV97ENguwUIgV8VUC31tMXOzkrd4ZX8RgXIDaOuqIPUgug6PlFoP7jbyp_v-SjE3i10phlOb2pYNvdjrBPs2P60U-L9IMs7wxiwIfkh9vdnSO7qJ_UmwnMhrB47hDsvB0s8zxEL90llKcWFVTpQXNejkAUv9On6MR1tBYmHTjRBbQgbGxdlhp5sfqjTZQ')
st_lib.set_configuration_uuid('52db99d3-edfb-44c5-b97a-f09df4402081')

tbl = Table("edac25ec-25e3-4949-9f49-d42124c26bf2", "52db99d3-edfb-44c5-b97a-f09df4402081", "bbb")
print (tbl.upload_data(r"data.csv"))
