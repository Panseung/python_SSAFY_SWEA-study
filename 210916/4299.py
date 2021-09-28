TC = int(input())
for tc in range(1, TC+1):
  D, H, M = map(int, input().split())
  DD, DH, DM = 11, 11, 11
  result = 0
  pot = 0
  if M - DM >= 0:
    pot += M - DM
  elif M - DM < 0:
    pot += 60 + M - DM
    H -= 1
  if H - DH >= 0:
    pot += (H - DH) * 60
  elif H - DH < 0:
    pot += (24 + H - DH) * 60
    D -= 1
  if D - DH >= 0:
    pot += (D - DH) * 24 * 60
  elif D - DH < 0:
    pot = -1
  print(f'#{tc} {pot}')