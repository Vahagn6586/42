/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/01 14:42:49 by vrafyan           #+#    #+#             */
/*   Updated: 2026/02/15 14:01:14 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	is_in_set(char const s1, char const *set)
{
	int	i;

	i = 0;
	while (set[i])
	{
		if (set[i] == s1)
		{
			return (1);
		}
		++i;
	}
	return (0);
}

char	*ft_strtrim(const char *s1, const char *set)
{
	int		i;
	int		j;
	int		it;
	char	*ptr;

	if (!s1 || !set)
		return (NULL);
	i = 0;
	it = 0;
	j = ft_strlen(s1) - 1;
	while (s1[i] && is_in_set(s1[i], set))
		++i;
	while (j > i && is_in_set(s1[j], set))
		--j;
	ptr = malloc(j - i + 2);
	if (!ptr)
		return (NULL);
	while (i <= j)
	{
		ptr[it] = s1[i];
		++it;
		++i;
	}
	ptr[it] = '\0';
	return (ptr);
}
