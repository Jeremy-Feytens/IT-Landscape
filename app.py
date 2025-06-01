import torch
import torch.nn as nn
import torch.optim as optim

torch.manual_seed(0)
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = 2 * x + 1 + 0.1 * torch.randn_like(x)

model = nn.Sequential(
    nn.Linear(in_features=1, out_features=1)
)

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

num_epochs = 50
for epoch in range(1, num_epochs + 1):
    preds = model(x)
    loss = criterion(preds, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0 or epoch == 1:
        w, b = model[0].weight.item(), model[0].bias.item()
        print(f"Epoch {epoch:2d}: loss={loss.item():.4f},  weight={w:.3f}, bias={b:.3f}")

test_x = torch.tensor([[4.0]])
pred_y = model(test_x)
print(f"\nModel prediction: for x=4.0 → y≈{pred_y.item():.3f} (true y=9.0)")
