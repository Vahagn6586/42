/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 15:34:33 by vrafyan           #+#    #+#             */
/*   Updated: 2026/02/11 17:21:19 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_memcmp(const void *val1, const void *val2, size_t count)
{
	size_t			i;
	unsigned char	*v1;
	unsigned char	*v2;

	i = 0;
	v1 = (unsigned char *)(val1);
	v2 = (unsigned char *)(val2);
	while (i < count)
	{
		if (*(v1 + i) != *(v2 + i))
		{
			return (*(v1 + i) - *(v2 + i));
		}
		++i;
	}
	return (0);
}
