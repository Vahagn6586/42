char	*ft_strstr(char *str, char *to_find);

char	*ft_strstr(char *str, char *to_find)
{
	int	i;

	if (*to_find == '\0')
		return (str);

	while (*str)
	{
		i = 0;
		while (*(str + i) && *(to_find + i) && *(str + i) == *(to_find + i))
			++i;
		if (*(to_find + i) == '\0')
			return (str);
		++str;
	}
	return (NULL);
}
