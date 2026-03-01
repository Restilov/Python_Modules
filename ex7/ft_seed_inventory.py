def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	messages = {
		"packets": "{} seeds: {} packets available",
		"grams": "{} seeds: {} grams total",
		"area": "{} seeds: covers {} square meters"
	}
	if unit in messages:
		print(messages[unit].format(seed_type.capitalize(),quantity))
	else:
		print("Unknown unit type")