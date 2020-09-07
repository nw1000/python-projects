


  def is_clicked(self):
    return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())